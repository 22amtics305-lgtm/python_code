x = "hello"
rev = x[::-1]

print(rev)
# string stored
s="hello"
print(s)
s=list(s)
print(s)
sorted_str=sorted(s)
print(sorted_str)
new_str="_" .join(sorted_str)
print(new_str)

print("-----------------")
#list
x=[10,20,30]
#access 20
print(x)
print(x[1])
#update :refvar[index]=new_value
print(x[2])
x[2]=300
print(x[2])


print("-----------------")
#loop
x=[10,20,30]
for items in x:
 print(items)
 
print("-----------------")
#add element by taking user ip first method 
x=[]
print(x)
for i in range(5):
      ip=input(f"enter{i+1} element:")
      x.append(ip)

print(x)
print("-----------------")
#extend
x=[1,2]
print(x)
x.extend([3,4])
print(x)
print("-----------------")
#insert(index,value)
x=[11,13]
#0 1---->0 1 2
x.insert(1,12)
print(x)
print("-----------------")
#remove(element)/pop(index)
x=[10,8,9,"hi",90,89];
x.remove("hi")
x.pop(4)
print(x)

print("-----------------")
#empty list
x=[]
x.clear
print(x)

print("-----------------")
#
x=[10,20,40,60,10,30]
print(x.count(10))
print(x.index(30))
x.sort
print(x)
x.reverse()
print(x)
y=x.copy()
print(y)

print("-----------------")

#function
x=[78,90,12,8]
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(sorted(x,reverse=True))
print("-----------------")

#count function
x=[10,20,45,30]
print(sum(x))
sum=0
for i in x:
    sum+=i
    print(sum)
    print(len(x))
count=0
for i in x:
    count+=1
    print (count) 
#max 
x=[10,20,30,40]
print(max(x))
max=0
for i in x:
    if i>max:
      max=i      
      
x=[10,20,30,40]
print(min(x))
min=0
for i in x:
    if i<min:
      min=i
print("-----------------")      
#student
student = [1, "ram", 45, 2, "sita", 78, 3, "pooja", 90]
print(student)
for i  in range(len(student)):
   if i%3==0:
      print(student[i])

print(student)
for i  in range(len(student)):
   if i%3==0: #0 1 2 3 4 5 6
      print(student[i+1])
   elif  i%2!=0:
      print(student[i])
for i  in range(len(student)):
   if i%3==0: #0 1 2 3 4 5 6
      print(student[i+2])    

#combine
for i in range(len(student)):
   if i%3==0:
      print(student[i])
      print(student[i+1])
      print(student[i+2])
      print("===========")


   
   
   
