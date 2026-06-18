#write a program of happy or sad number
num = 28
temp = num

while num != 1 and num != 4:
    sum = 0

    while num > 0:
        rem = num % 10
        sum = sum + rem ** 2
        num = num // 10

    num = sum

if num == 1:
    print(temp, "is a Happy Number")
else:
    print(temp, "is a Sad Number")
#write a program to print pattern   

n = int(input("enter number\n"))
i =1
while i<=n:
    j = 1
    while j<=i:
        print("*",end=" ")
        j = j+1
    print()
    i = i+1
#write a program to print For pattern

print("ENTER FOR PATTERN")
for i in range (n):
  for j in range (n):
    print("*",end="")
  print()

  #Write a program to print number pattern

n = 5
print("ENTER NUMBER PATTERN")
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()

    #write a program to print star pattern
n = 5
print("ENTER STAR PATTERN")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()


n=4
num=1
print("ENTER NUMBER PATTERN")
for i in range(n):
    for j in range(i + 1):
        print(num, end=" ")
        num = num + 1
    print()

    #write a program to print x pattern
n = 5
print("ENTER X PATTERN")
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()