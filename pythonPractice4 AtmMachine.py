class Atm:
    def __init__(self):
        self.balance=0
        self.pin=""
        self.menu()

    def menu(self):
        while(True):
       
            user_input=input("""
                How would you like to  proceed
                1. Enter 1 to create pin
                2. Enter 2 to check balance
                3. Enter 3 to deposit money
                4. Enter 4 to withdraw money
                5. Enter 5 to exit 
                """)
       
        
            if user_input=="1":
                self.create_pin()

            elif user_input=="2":
                self.check_balance()
            elif user_input=="3":
                self.deposit()
            elif user_input=="4":
                self.withdraw()
            else:
                print("thanks for using")
                break
                   
            
    def create_pin(self):
        self.pin=input("enter pin ")
        print("pin create successfully")

    def check_balance(self):
        temp=input("Enter your pin ")
        if temp==self.pin:
            print(self.balance)

    def deposit(self):
        temp = input("Enter your pin ")
        if temp==self.pin:
            amount=int(input("enter amount "))
            self.balance=self.balance + amount
            print("amount deposit successfully")
        else:
            print("invalid pin")

    def withdraw(self):
        temp = input("Enter your pin ")
        if temp == self.pin:
            amount = int(input("enter amount "))
            if amount < self.balance:
                self.balance= self.balance - amount
                print("money successfully withdraw")
            else:
                print("Insufficient balance")
        else:
            print("invalid pin")
    


sbi=Atm()





