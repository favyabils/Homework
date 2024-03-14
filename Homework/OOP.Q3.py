w = 3
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
         self.account_number = account_number
         self.balance = balance
         self.date_of_opening = date_of_opening
         self.customer_name = customer_name

    def deposit(self,amount):
        self.balance += amount
        print("{} has been deposited in your account.".format(amount))
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("{} has been withdrawn from your account.".format(amount))

    def check_balance(self):
        print("Your current balance is .".format(self.balance))


Customer_1 = BankAccount(1287435682, 100000, "01-01-2011", "Esther Mark")
Customer_2 = BankAccount(9045263233, 20000, "11-03-2011", "John Doe")
Customer_3 = BankAccount(2972742018, 305600, "12-01-2009", "Joshua Nakase")
Customer_4 = BankAccount(5937280375, 843000, "01-01-2011", "Brian Eslow")
Customer_5 = BankAccount(4890247377, 784000, "01-05-2011", "Kentucky Freedman")       

Customer_1.deposit(3044)
print(Customer_1.balance)
Customer_2.deposit(78000)
print(Customer_2.balance)


Customer_3.withdraw(20000000)
Customer_4.withdraw(3000)
print(Customer_4.balance)

Customer_5.check_balance