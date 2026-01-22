from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import cloudtableserializer
from django.shortcuts import render
from .models import cloudtable
import cloudinary
import datetime
import bcrypt
import json
import jwt
import re
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
SECRETKEY = settings.SECRET_KEY

# Create your views here.

############## validate ##############
def is_valid_user(req):
    try:
        cookei_token=req.COOKIES.get("my_first_cookie")
        # print(cookei_token)
        data=jwt.decode(jwt=cookei_token,key=SECRETKEY,algorithms=["HS256"])
        # print(data)
        return data
    except:
        return False
        # return HttpResponse("no cookei found!")

############## Register User ##############

# @csrf_exempt
# def reg_user(req):
#     user_data=json.loads(req.body)
#     # ORM- oblect relational maping
#     new_user=cloudtable.objects.create(id=user_data['id'],name=user_data['name'],email=user_data['email'],mobile=user_data['mob'])
#     return JsonResponse({'status':'user created sucessfully'})

#------------------------------------------------------------------------------------------

@csrf_exempt
def reg_user(req):
    if req.method =='POST':
        try:
            sid=req.POST.get('id')
            sname=req.POST.get('name')
            semail=req.POST.get('email')
            smobile=req.POST.get('mobile')
            sphoto=req.FILES.get('photo')
            spass=req.POST.get('password')
            #------- Basic validation --------#
            if not all([sname,semail,spass]):
                return JsonResponse({"error":"name,email, and password are required"}, status=400)
            #------- cloudinary code --------#
            img_url=None
            if sphoto:
                upload_result=cloudinary.uploader.upload(
                    sphoto,
                    folder="student_pic", #all images go here
                    use_filename=True,    #keeps original filename
                    unique_filename=True, #adds unique ID if name repeate
                    overwrite=False
                    )
                img_url=upload_result.get("secure_url")
                
            #print(img_url['secure_url'])
            #------- bcrypt code --------#
            no_salt=bcrypt.gensalt(rounds=14)
            # print(no_salt)
            #print(f"user input: {spass,type(spass)}")
            spass=spass.encode('utf-8')
            hashed_pass=bcrypt.hashpw(password=spass,salt=no_salt)
            #print(f"Before Hashing: {spass} \n After Hashing: {hashed_pass}")
            hashed_pass=hashed_pass.decode('utf-8')
            #print(f"After Decode: {hashed_pass}")
    
            new_user=cloudtable.objects.create(id=sid,
                                            name=sname,
                                            email=semail,
                                            mobile=smobile,
                                            photo=img_url,
                                            password=hashed_pass)
            data = cloudtableserializer(new_user).data
            send_mail(subject="requstered sucessfully",
            message="You have successfully created your account in env_pro app",
            recipient_list=[semail],
            from_email=settings.EMAIL_HOST_USER
        )
            return JsonResponse({'status':'user created sucessfully','detsils':data})
        except Exception as e :
            return JsonResponse({"error":str(e)},status=400)
    return JsonResponse({"error":"Only POST method allowed"},status=405)

############## Get user ##############

def get_user(req,id=None):
    if is_valid_user(req)["valid_user"]or id==is_valid_user(req)["id"]:
        if req.method=="GET":
            try:
                user_details=cloudtable.objects.get(id=id)
                serialized_data=cloudtableserializer(user_details,many=False)
                return JsonResponse({'User Details':serialized_data.data})
            except cloudtable.DoesNotExist:
                return JsonResponse({"error":"user not found"},status=404)
        else:
            return JsonResponse({"error":"Only 'GET' method alloewd"},status=405)
    else:
        res = HttpResponse("invalid user details")
        res.delete_cookie("my_first_cookie")
        return res  
    
#-------------------------------------------------------------------------------

def get_users(req):
    if is_valid_user(req)["valid_user"]:
        if req.method=="GET":
            user_details=cloudtable.objects.all()
            serialized_data=cloudtableserializer(user_details,many=True)
            return JsonResponse({'User Details':serialized_data.data})
        else:
            return JsonResponse({"error":"Only 'GET' method alloewd"},status=405)
    else:
        res = HttpResponse("invalid user details")
        res.delete_cookie("my_first_cookie")
        return res

############## Update User ##############

# @csrf_exempt
# def update_user(req,id):
#     if is_valid_user(req)["valid_user"] or id==is_valid_user(req)["id"]:
#         if req.method=="PUT":
#             try :
#                 old_data=cloudtable.objects.get(id=id)

#                 #check if content type is multipart (for files) or json
#                 if req.contant_type.startswith("multipart/form-data"):
#                     new_data=req.POST
#                     new_image=req.FILES.get("photo")
#                 else:
#                     new_data=json.loads(req.body)
#                     new_image=None

#                 # update baasic fields
#                 old_data.name=new_data.get("name",old_data.name)
#                 old_data.email=new_data.get("email",old_data.email)
#                 old_data.mobile=new_data.get("mobile",old_data.mobile)

#                 # update password (hash it again if provided)
#                 new_pass=new_data.get("password")
#                 if new_pass:
#                     hashed_pass= bcrypt.hashpw(new_pass.encode("utf-8"),bcrypt.gensalt(14).decode("utf-8"))
#                     old_data.password=hashed_pass
                    
#                 #replace old image with new image if provided
#                 if new_image:
#                     # if user already has a photo, delete it from cloudinary
#                     # if old_data.photo:
#                     #     old_data.photo.delete()
#                     if old_data.photo:
#                         try:
#                             # Extract public_id from the URL using regex
#                             match = re.search(r"user_profile_pic/([^\.]+)", old_data.photo)
#                             if match:
#                                 public_id = f"user_profile_pic/{match.group(1)}"
#                                 cloudinary.uploader.destroy(public_id)
#                         except Exception as e:
#                             print("Warning: Failed to delete old image:", str(e))
#                     # upload new image
#                     upload_result = cloudinary.uploader.upload(
#                         new_image,
#                         folder="users_folder",
#                         use_filename=True,
#                         unique_filename=True,
#                         overwrite=True
#                     )
#                     old_data.photo = upload_result.get("secure_ur1")
#                 old_data.save()
#                 serializer = cloudtableserializer(old_data)
#                 return JsonResponse ({"msg": "User updated successfully", "user": serializer. data},status=200)
#             except cloudtable.DoesNotExist:
#                 return JsonResponse({f"error": "User not found"}, status=404)
#             except Exception as e:
#                 return JsonResponse({f"error": str(e)}, status=400)
#         return JsonResponse({f"error": "Only PUT method allowed"}, status=405)
#     else:
#         res = HttpResponse("invalid user details")
#         res.delete_cookie("my_first_cookie")
#         return res
 
#-------------------------------------------------------------------------------

@csrf_exempt
def update_user(req,id):
    if is_valid_user(req)["valid_user"]:      
        old_data=cloudtable.objects.get(id=id)
        new_data={}
        for field in req.POST:
            new_data[field]=req.POST[field]
        serialized_data=cloudtableserializer(old_data,data=new_data,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse('user updated sucessfully')
    else:
        res = HttpResponse("invalid user details")
        res.delete_cookie("my_first_cookie")
        return res

############## Delete User ##############

@csrf_exempt
def delete_user(req,id=None):
    if is_valid_user(req)["valid_user"]:
        if req.method=="DELETE":
            try:
                del_user=cloudtable.objects.get(id=id)
                del_user.delete()
                send_mail(subject="Account Deleted",
                          message="Your X app account has been deleted successfully.",
                          recipient_list=[del_user.email],
                          from_email=settings.EMAIL_HOST_USER
                        )
                return JsonResponse({"error" : "user deleted sucessfully"})
            except cloudtable.DoesNotExist:
                return JsonResponse({"error" : "user not found"},status=404)
        return JsonResponse({"error" : "Only DELETE method allowed"},status=405)
    else:
        res = HttpResponse("invalid user details")
        res.delete_cookie("my_first_cookie")
        return res

#-------------------------------------------------------------------------------

# def delete_user(req,id):
#     if req.method=="DELETE":
#         try:
#             del_user=cloudtable.objects.get(id=id)
#             del_user.delete()
#             return JsonResponse({"error" : "user deleted sucessfully"})
#         except cloudtable.DoesNotExist:
#             return JsonResponse({"error" : "user not found"},status=404)
#     return JsonResponse({"error" : "Only DELETE method allowed"},status=405) 

############## login User ##############

def login_user(req):
    credentials=json.loads(req.body)
    user=cloudtable.objects.get(id=credentials["id"])
    serialized_data=cloudtableserializer(user).data
    #print(serialized_data)
    encrypted_pass=serialized_data["password"]
    entered_pass=credentials["password"]
    is_same=bcrypt.checkpw(entered_pass.encode("utf-8"),encrypted_pass.encode("utf-8"))

    # print(is_same)
    #creating jwt
    # -> encode -> payload="", key="", algorithm="HS256" -> token (encoded sting)
    # -> decode -> jwt="token", key="", algorithm="HS256" -> payload

    user_payload={
        # "name" : "nishanth",
        # "email" : "nishanth@gamil.com",
        "name": serialized_data["name"],
        "email" : serialized_data["email"],
        "id" : serialized_data["id"],
        "valid_user" : True,
        "exp" : datetime.datetime.utcnow()+datetime.timedelta(seconds=20),
        "iat" : datetime.datetime.utcnow(),
    }     
    token=jwt.encode(payload=user_payload,key=SECRETKEY,algorithm="HS256")
    # print(token)
    # user_data=jwt.decode(jwt=token,key=SECRETKEY,algorithms="HS256")
    # print(user_data)

    # if is_same:
    # if 1:
    if is_same:
        res=HttpResponse("cookie is set in browser")
        res.set_cookie(
            key="my_first_cookie", #cookei name
            value=token, #string data
            # httponly=True, #allowes js to access
            max_age=3000 #life time in sec
        )
        return res
    else:
        return HttpResponse("Wrong Credentials")
    
    # if is_same:
    #     return HttpResponse(f"wellcome to the app {user.name}")
    # else:
    #     return HttpResponse("Wrong Credentials")
@csrf_exempt
def send_file(req):
    user_email=req.POST.get("email")
    pic=req.POST.get("file")
    email=EmailMessage(
        subject="Sending File",
        body="your file is here.",
        from_email=settings.EMAIL_HOST_USER,
        to=[user_email],
    )
    email.attach_file(pic)
    email.send()
    return HttpResponse("Email sent sucessfully")
