class Account:
    def __init__(self, balance):
        self.__balance = balance
    def deposite(self, amount):
        if amount>0:
            self.__balance += amount
    def show(self):
        print("Balance is", self.__balance)
    def get_balance(self):
        return self.__balance

account1 = Account(1000)
account1.deposite(5000)
account1.show()

print(account1.get_balance())