units_consume = int(input("Enter the electricity units consumed: "))

if units_consume >= 0 and units_consume < 50:
    electricity_bill = 0

elif units_consume >= 50 and units_consume < 100:
    electricity_bill = (units_consume - 50) * 5

elif units_consume >= 100 and units_consume < 150:
    electricity_bill = 50 * 5 + (units_consume - 100) * 10

elif units_consume >= 150 and units_consume < 200:
    electricity_bill = 50 * 5 + 50 * 10 + (units_consume - 150) * 15

elif units_consume >= 200:
    electricity_bill = 50 * 5 + 50 * 10 + 50 * 15 + (units_consume - 200) * 20

else:
    print("Please enter valid units consumed")
    electricity_bill = 0

print("Your electricity bill is {} Rs".format(electricity_bill))