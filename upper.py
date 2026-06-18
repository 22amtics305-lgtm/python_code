#? checking methods----->true/flase
X ="hello"
print(X.isupper())
print(X.islower())
# check--------->all alphabets
print(X.isalpha())

X ="1234"
print(X.isdigit())

#alpha+num
X="a1234"
print(X.isalnum)
print(X.startswith("al"))
print(X.startswith("cal"))
print(X.endswith("4"))

#while spaces-------->remove
X="hello"
print(len(X)) #7
X=X.strip()
print(len(X))

# write a proogram of string to count 

str=input("enter to string to check count\n")
ip= input("enter char to check\n")
ct = 0
for ch in str:
    if ch==ip:
        ct+=1
        print(ct)
