#activity_02

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # private attribute
 
    def get_balance(self):
        return self.__balance
 
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
 
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient balance!")
            return
        self.__balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{self.__balance}")
 
# Example usage:
acc = BankAccount(1000)
print("Initial balance:", acc.get_balance())
 
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)  # Should warn insufficient balance
acc.deposit(-50)    # Should warn invalid deposit
