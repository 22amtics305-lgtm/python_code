class Product:
    def __init__(self, name, brand, mfg, exp, qty, price):
        self.name = name
        self.brand = brand
        self.mfg = mfg
        self.exp = exp
        self.qty = qty
        self.price = price


# Products
p1 = Product("Laptop", "HP", "01-01-2025", "01-01-2030", 10, 50000)
p2 = Product("Mobile", "Samsung", "10-02-2025", "10-02-2030", 20, 20000)
p3 = Product("Headphone", "Boat", "15-03-2025", "15-03-2030", 15, 1500)

products = [p1, p2, p3]


while True:

    print("\n===== PRODUCT MANAGEMENT =====")
    print("1. All Product Details")
    print("2. Search Product")
    print("3. Purchase Product")
    print("4. Exit")

    choice = input("Enter Choice: ")

    # ---------------- All Details ----------------
    if choice == "1":
        print("\nProduct List")
        for p in products:
            print("------------------------")
            print("Name     :", p.name)
            print("Brand    :", p.brand)
            print("MFG Date :", p.mfg)
            print("EXP Date :", p.exp)
            print("Quantity :", p.qty)
            print("Price    :", p.price)