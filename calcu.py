def calculate(num1,num2,operation):
    if operation=='1':
        return num1+num2
    elif operation=='2':
        return num1-num2
    elif operation=='3':
        if num2!=0:
             return num1*num2
        else:
            return "Error:Cannot Multiply by zero"
    elif operation=='4':
        if num2!=0:
            return num1/num2
        else:
            return "Error:Cannot divide by zero"
    else:
        return "Invalid Operation"

print("--- Mini Calculator ---")
n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))

print("Choose one:")
print("1.add\n2.sub\n3.multi\n4.divion")
choice = input("Enter your choice: ")

result = calculate(n1, n2, choice)
print(f"Result is: {result}")
print("----------------------------------")