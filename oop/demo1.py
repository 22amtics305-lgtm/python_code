class demo:
    #inst var --> __init__
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        
    #ins method
    def welcome(self):
        return "hello students !"
        
    def modify(self):
        newvalue=input("enter new name\n")
        #print(f"existing name:(self.name))
        ex_name=self.name
        self.name=newvalue
        print(f"existing name {ex_name} updated name {self.name}")
            
s1=demo("Ram",101,21)
print(s1.name,s1.id,s1.age)        
print(s1.welcome())
s1.modify()