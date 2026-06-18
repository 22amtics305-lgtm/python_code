#pattern1
for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

print()   # <-- gap
#pattern2

for i in range(3):
    for j in range(3):
        print(chr(97 + i), end="")
    print()

print()   # <-- gap
#pattern3

ch = 97

for i in range(3):
    for j in range(4):
        print(chr(ch), end="")
        ch += 1
    print() 

print()   # <-- gap
#pattern4
num = 9

for i in range(3):
    for j in range(3):
        print(num, end="")
        num -= 1
    print()

print()   # <-- gap
#pattern5

ch = 65

for i in range(3):
    for j in range(3):
        print(chr(ch), end=" ")
        ch += 2
    print()

print()   # <-- gap
#pattern6
for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()        

print()   # <-- gap

#pattern7
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("O", end=" ")
        else:
            print("1", end=" ")
    print()