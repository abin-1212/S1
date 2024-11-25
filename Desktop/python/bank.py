
class Bank:
    def __init__(self, accno, name, acc_type):
        self.accno = accno
        self.name = name
        self.type = acc_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount: ", amount)
        print("Available balance: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!!!")
        else:
            self.balance -= amount
            print("Withdrawn amount: ", amount)
            print("Available balance: ", self.balance)

    def display(self):
        print("Available Balance is: ", self.balance)


# Input account details
accno = int(input("Enter your account number: "))
name = input("Enter your name: ")
acc_type = input("Enter your type of account: ")
member = Bank(accno, name, acc_type)

# Menu-driven interface
while True:
    choice = int(input("\nEnter your choice:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n"))
    if choice == 1:
        amount = int(input("Enter the amount to be deposited: "))
        member.deposit(amount)
    elif choice == 2:
        amount = int(input("Enter the amount to be withdrawn: "))
        member.withdraw(amount)
    elif choice == 3:
        member.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
