#no return type no argument
def greet():
    print("welcome user!")
    #100
greet()# fuction call--->funct_name
greet()   


#no return type with argument
def greet1(name):
    print("welcome",name)
name=input("enter your name")
greet1(name)

#with return type without argument
def getno():
      return 10**2
print(getno())

#value use
op=getno()
print(op)
op+=2
print(op)


def cube(num):
     return num**3
num=int(input("enter no\n"))
print(cube(num))
op=cube(num)
print(op)

#addition of two number using function 
def add(a,b):
     print(a+b)
add(10,20)  

#*args
def add1(*args):
     print(sum(args))
     print(type(args))
add1(1,2,3,5765,90)  

def info(name,age,marks):
     return f"name:{name}\nage:{age}\nmarks:{marks}"
name=input("enter your name")
age=int(input("enter your age"))
marks=float(input("enter your marks"))
print(info(name,age,marks))
