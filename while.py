num = 1234
ct = 0
while num>0:
    num = num//10
    ct = ct+1
print(ct)
num = 1234
rev = 0
while num>0:
    rem = num%10
    rev = rev * 10 + rem
    num = num//10
print(rev)

num = int(input("enter number\n"))
rev = 0
while num>0:
    rem = num%10
    rev = rev * 10 + rem
    num = num//10
if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
num = int(input("enter number\n"))
Temp = num
sum = 0
ct=0
while temp>0:
    ct=ct+1
    temp = temp//10
print(ct)
temp = num
while temp>0:
    rem = temp%10
    sum = sum + rem**ct
    temp = temp//10
if sum == num:  
    print("Armstrong")
else:
    print("Not an Armstrong")
 