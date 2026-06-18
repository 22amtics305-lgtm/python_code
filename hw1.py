x=[10,57,6,98,32,10,57,98]
print(x)
ip=int(input("enter your key to find"))
flag=0
for i in x:
    if ip==1:
        print("key found")
if flag==0:
    print("key not found")  

      
#Duplicate Elements
X = [10,57,6,98,32,10,57,98]
print(X)
print("duplicate keys")
y=[]
for i in X:
    if X.count(i) > 1 and i not in y:
        print(i)
        y.append(i)

print()   # blank line

#Unique Elements

X = [10,57,6,98,32,10,57,98]
print(X)
print("unique element")
for i in X:
    if X.count(i) <= 1:
        print(i)
print()   # blank line

#Sorting
X = [10,57,6,98,32]

X.sort()

print(X)
                
print()   # blank line

#Even and Odd Count

X = [10,57,6,98,32]

even = 0
odd = 0

for i in X:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)