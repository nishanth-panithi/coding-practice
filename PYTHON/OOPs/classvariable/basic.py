class mobile:
    fetures={"battery":"5000mah-24w","display":"oled","processor":"8gen+","ip":"68","Bcamera":"48mp-4K60fps","Fcamera":"24mp-4k30fps"}
m1=mobile()
print(m1.fetures)
###

class mobile:
    fetures={"battery":"5000mah-24w","display":"oled","processor":"8gen+","ip":"68","Bcamera":"48mp-4K60fps","Fcamera":"24mp-4k30fps"}
    def creat():
        return "mobile is ready"
m1=mobile()
print(m1.creat())
print(mobile().creat())
print(m1.fetures)
###

class mobile:
    def __init__(self,price,battery,display,processor,ip,bc,fc):
        self.price=price
        self.battery=battery
        self.display=display
        self.processor=processor
        self.ip=ip
        self.bc=bc
        self.fc=fc
    def details(self):
        return f"{self.price,self.battery,self.display,self.processor,self.ip,self.bc,self.fc}"
m1=mobile("10k","5000","oled","8gen+","68","48mp","24mp")
print(m1)
print(m1.details())
print(m1.price)
m2=mobile("20k","4000","oled","7gen+","67","48mp","24mp")
print(m2.processor)