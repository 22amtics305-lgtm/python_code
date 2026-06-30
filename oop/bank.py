class bank:
    #class var
    bankname="SBI"
    ifsc="SBI001"

    #instance var
    def __init__(self,name,bal,mail,):
        self.name=name
        self.bal=bal
        self.mail=mail
    

    #method ins
    def show_details(self):
        print(f"name:{self.name}\nbal:{self.bal}\nemailid:{self.mail}\nbankname:{self.bankname}\nifsc:{self.ifsc}")

    def check_bal(self):
        print("avail bal is ",self.bal)

    def deposit(self,amount):
        amount=int(input("enter amount to deposit:"))
        if amount>0:
            self.bal+=amount
            print(f"Rs {amount} is deposited to your account :{self.bal}")
        else:
            print("amount should be greater than 0")
    def withdraw(self):
        amount=int(input("enter amount to deposit:"))
        if amount<self.bal:
            self.bal-=amount
            print(f"Rs {amount} is deposited and available balance is {self.bal}")
        else:
            print("insufficient balance")
    

user1=bank("ram", 0, "ram123@gmail.com")
user1.show_details()
user1.deposit
user1.check_bal()
user1.withdraw()
user1.