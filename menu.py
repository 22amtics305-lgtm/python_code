menu = ((1,"panner",400),(2,"pizza",500),(3,"icecream",200),(4,"noodles",200))
orders = []
while True:
    print("-------hotel menu------\n1.view menu\n2.order\n3.view order\n4.generate bill\n5.exit")
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            for item in menu:
                print(f"{item[0]} {item[1]} {item[2]}")
        case 2:
           item_id = int(input("Enter item ID to order: "))
           for item in menu:
                if item[0] == item_id:
                    qty = int(input(f"Enter quantity for {item[1]}: "))
                    amount = qty * item[2]
                    orders.append((item[1], qty, item[2], amount))
                    print(f"Added {item[1]} to your order.")
        
        case 3:
          print("\n--- Your Current Order ---")
          for o in orders:
                print(f"Item: {o[0]} | Qty: {o[1]} | Subtotal: {o[3]}")
        
        case 4:
            total = sum(item[2] for item in menu)
            print(f"\nTotal Bill: {total}")
            
        case 5:
            print("Exiting...")
        case 5:
           print("Thank You!!! visit Again")