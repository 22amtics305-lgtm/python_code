

fruit=["apple","banana","grapes"]
for x in fruit:
    print(x,end=" ")
    print()
no=[1,2,3,4,5]
for x in no:
    print(x)
#string value
s="india"
for x in s:
    print(x)
#printing 1 to 5
for i in range(1,6):
    print(i)

#reversing a 21-11
for i in range(21,10,-1):
    print(i)

#printing numbers divisible by 5 and 7
start=int(input("enter starting number\n"))
end=int(input("enter ending number\n"))
for i in range(start, end + 1):
    if i%5==0 and i%7==0:
        print(i)

#1-5 -->3
for i in range(1,6):
    if i==3:
        print("thank you")
        break;

#1-5 -->4-->1 2 3 5
for i in range(1,6):
    if i==4:
        continue;
    print(i)

#sum of no. from 23 to 58
sum=0
for i in range(23, 59):
    sum=sum+i
print("sum is",sum)

#print table of no. by user input
n=int(input("enter number for table\n"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

#write a program to print even no. from 501 to 103 in reverse order
for i in range(500, 102, -1):
    if i%2==0:
        print(i)

#write a program factor of 5 betwwen 1 to 5
for i in range(1,6):
    if 5%i==0:
        print(i)


#write a program of factoiral 7 
fact=1
for i in range(1, 8):
    fact=fact*i 
print(f"Factorial of 7 is: {fact}"