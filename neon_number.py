num = int(input("Enter a number: "))

square = num * num
sum = 0

while square > 0:
    digit = square % 10
    sum = sum + digit
    square = square // 10

if sum == num:
    print(num, "is a Neon Number")
else:
    print(num, "is not a Neon Number")
