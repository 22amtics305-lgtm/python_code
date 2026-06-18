# 1 Reverse String
x = "hello"
print("Reverse =", x[::-1])

# 2 Count Even, Odd and Print Vowels
x = "mahareshshinde"

even_count = 0
odd_count = 0
vowels = ""

for ch in x:
    if ch.lower() in "aeiou":
        vowels += ch

for i in range(len(x)):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even position characters =", even_count)
print("Odd position characters =", odd_count)
print("Vowels =", vowels)

# 3 convert string Uppercase
x = "hello"
print(x.upper())

# 4 Remove Whitespace and find Length
x = " hey "
x = x.strip()
print("String =", x)
print("Length =", len(x))

# 5 Replace p with x
x = "python_programming"
print(x.replace("p", "x"))

