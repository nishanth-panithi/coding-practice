import otp as o
def changepass(oldpass, newpass, uotp):
    sotp=o.otp()
    opass="nani"
    if oldpass==opass and uotp==sotp:
        opass=newpass 
        print("password change is sucesssful")
    else:
        print("failed to change password")
print(o.otp())    
op=input("enter old password:")
np=input("enter new password:")
motp=input("enter otp:")
changepass(op,np,motp)