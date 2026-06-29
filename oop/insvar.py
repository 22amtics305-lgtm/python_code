class Demo:
    # Instance variables
    def __init__(self):
        self.name = "ram"
        self.age = 20

obj = Demo()

print(obj.name)
print(obj.age)


#========================dy_value====================
class mobile:
     def __init__(self,uname,ubrand,ucolour,uprice):
         self.name=uname
         self.brand=ubrand
         self.colour=ucolour
         self.price=uprice

#obj
obj=mobile("iphone15","iphone","black","100")
print(obj.name,obj.colour,obj.price)         

obj1=mobile("iphone15","iphone","pink","200")
print(obj1.name,obj1.colour,obj.price)         

x=[obj,obj1]
for i in x:
    print(i.name)
