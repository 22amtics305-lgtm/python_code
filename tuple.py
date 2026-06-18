x=(10,20,30)
print(x,type(x))
print(x[2])
#x[2]=300
#print(x[2])
for i in x:
    print(x)
    x=("red","pink","black")
    print("red" in x)
    print("gray" in x)

x=(10,20)
y=(10,20,90)
z=x
print(x is y)
print(x is z)


x=(10,20,30)
a,b,c=x
print(a,b,c)
print("-------------------")

print(len(x))
print(x.count(20))
print(x.index(30))
print(x[1:])
print(x[1:2])

print("-------------------")

x=((10,20),30,(40,50),"hi")
for i in x:
    if type(i)==tuple:
        for j in i:
             print(j)
        continue
    print(i)     
print("-------------------")
#x=[10,[20,30],40(50,60)]
#print(x[2])
#print(x[3][0])
#print(x[1][1])

for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            print(j)
        continue
    print(i)

print("-------------------")

x=(90,"hi",("red",[10,20]),[100,200])
for i in x:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==list:
                for k in j:
                    print(k)
                    continue
                print(j)
                continue
            print(i)

print("-------------------")

x=(10,20)
print(x,type(x))
y=list(x)
y.append(90)
print(y,type(x))
x=tuple(y)
print(x,type(x))


       

