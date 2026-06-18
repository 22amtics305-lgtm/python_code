#REVESER
X="india"
print(X[3:5])
print(X[3:])
print(X[0:3])
print(X[:3])
print(X[1:4])
print(X[0:5:2])

##2
X ="india is my country!"
#is
#count
#s m
#try!
print(X[6:8])
print(X[12:17])
print(X[7:10])
print(X[16:])
print(X[-10:-15:-1])
print("----------------------------------------")
#reverse 
ip= input("enter here\n")
if ip==ip[::-1]:
    print("pall")
else:
    print("not pall")
print("----------------------------------------")

X ="abcd1234"
ct1=0
ct2=0
for i in X :
    if i>='0' and i<='9':
        ct1+=1
    elif i.isalpha():
          ct2+=1
print("count of digit is",ct1)
print("count of digit is",ct2)
print("----------------------------------------")
#a
X="hello"
new_str=""
for i in X:
    if i>='a' and i<='z':
        new_str+chr(ord(i)-32)
        print(new_str)

#swapcase --------------->swapcase
X="swapcase"
new=""
for i in X:
    if i>='a' and i<='z':
        new+=chr(ord(i)-32)
    elif i>='A' and i<='z':
        new+=chr(ord(i)+32)
print(new)

X="programming"
#even char
for i in X:
    if ord(i)%2!=0:
        print(i,ord(i))
#5
X="hii"
print(len(X))
new=" "
for ch in X:
    if '' not in ch:
        new+=ch
print("ans", new,len(new))


X="Programming"
unique=" "
for ch in X:
    if ch not in unique:
        unique+=ch
        print(unique)

X=" I LIKE PYTHON PROGRAMMING"
ct=1
for ch in X:
        if' '==ch:
            ct+=1
print(ct)




       




      





      

      



    




