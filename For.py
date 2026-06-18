#pattern1

import code


for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
print("------------")
# pattern2
for i in range(1, 5):
    if i % 2 != 0:
        print("1" * i)
    else:
        print("0" * i)
print("------------")
        #pattern3
num = 1
for i in range(1, 5):
    print(str(num) * i)
    num += 2
print("------------")
    #pattern4

for i in range(1, 5):
    num = i * i
    for j in range(i):
        print(num, end="")
    print()
print("------------") 
    #pattern5
n = 4
for i in range(n):
    print("0" * (n - i - 1) + "1")
print("----------")

#pattern6
#pattern6
n = 5

for i in range(n):
    for j in range(n):
        if j == 0 or (i == 0 and j < n-1) or (i == n//2 and j < n-1) or (j == n-1 and i > 0 and i < n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("------------") 
    #pattern7
for i in range(1, 4):
     print("* " * i)

for i in range(2, 0, -1):
    print("* " * i)
    print()
print("------------") 
    #pattern8
# Upper part
for i in range(1, 8, 2):
    print(str(i) * ((i + 1) // 2))

# Lower part
for i in range(5, 0, -2):
    print(str(i) * ((i + 1) // 2)) 