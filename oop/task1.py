class Product:
    def __init__(self, pid, name, category, brand, mfg, exp, qty, price):
        self.pid = pid
        self.name = name
        self.category = category
        self.brand = brand
        self.mfg = mfg
        self.exp = exp
        self.qty = qty
        self.price = price


class DMart:

    def __init__(self):
        self.products = [
            Product(1, "Rice", "Grocery", "Fortune", "01-01-2026", "01-01-2027", 20, 60),
            Product(2, "Milk", "Dairy", "Amul", "10-06-2026", "20-06-2026", 15, 35),
            Product(3, "Biscuit", "Snacks", "Parle-G", "01-02-2026", "01-02-2027", 25, 10),
            Product(4, "Sugar", "Grocery", "Madhur", "01-03-2026", "01-03-2027", 18, 45)
        ]

        self.cart = []

    def show_products(self):
        print("\n----------- PRODUCT LIST -----------")
        print("ID\tName\t\tQty\tPrice")

        for p in self.products:
            print(p.pid, "\t", p.name, "\t\t", p.qty, "\tRs.", p.price)

    def search_product(self):
        name = input("Enter Product Name : ")

        found = False

        for p in self.products:
            if p.name.lower() == name.lower():
                print("\nProduct Found")
                print("ID :", p.pid)
                print("Name :", p.name)
                print("Category :", p.category)
                print("Brand :", p.brand)
                print("MFG :", p.mfg)
                print("EXP :", p.exp)
                print("Quantity :", p.qty)
                print("Price : Rs.", p.price)
                found = True

        if found == False:
            print("Product Not Found")

    def purchase_product(self):

        self.show_products()

        pid = int(input("Enter Product ID : "))

        for p in self.products:

            if p.pid == pid:

                qty = int(input("Enter Quantity : "))

                if qty <= p.qty:
                    p.qty = p.qty - qty
                    self.cart.append([p, qty])
                    print("Product Added Successfully")
                else:
                    print("Stock Not Available")
                return

        print("Invalid Product ID")

    def bill(self):

        if len(self.cart) == 0:
            print("Cart is Empty")
            return

        total = 0

        print("\n=========== BILL ===========")
        print("ID\tName\t\tQty\tPrice\tAmount")

        for item in self.cart:
            product, qty = item
            amount = product.price * qty
            total += amount
            print(product.pid, "\t", product.name, "\t\t", qty, "\tRs.", product.price, "\tRs.", amount)

        print("\nTotal Amount : Rs.", total)
        print("============================")


shop = DMart()

while True:

    print("\n====== DMART MENU ======")
    print("1. Show Products")
    print("2. Search Product")
    print("3. Purchase Product")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        shop.show_products()

    elif choice == "2":
        shop.search_product()

    elif choice == "3":
        shop.purchase_product()

    elif choice == "4":
        shop.bill()

    elif choice == "5":
        print("Thank You...")
        break

    else:
        print("Invalid Choice")