

class Bank():
    def __init__(self):
        self.name = "Karan"
        self.__balance = 11000

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

b = Bank()
print(b.name)
b.deposit(500000)
print(b.get_balance())

