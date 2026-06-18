menu = ((1, "Pizza", 150), (2, "Burger", 100), (3, "Sandwich", 80), (4, "Coffee", 50))
orders = []

while True:
    print("---------Hotel MENU------\n1.View Menu\n2.Order\n3.Generate Bill\n4.Exit\n")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Items are:\n-------------\nitem id name price\n----------")
            for item in menu:
                print(f"{item[0]} {item[1]} {item[2]}")
        case 2:
            item_id = int(input("Enter Item ID: "))
            qty = int(input("Enter Quantity: "))
            found = False
            for item in menu:
                if item[0] == item_id:
                    amount = item[2] * qty
                    orders.append((item[1], qty, item[2], amount))
                    print(f"{item[1]} added successfully!")
                    found = True
                    break;         
        case 3:
            print=("\n--------------your order---------------")
            for order in orders:
             print(f"items")
        case 4:
            print("Thank You! Visit again!")
            break
        case _:
            print("Invalid choice")