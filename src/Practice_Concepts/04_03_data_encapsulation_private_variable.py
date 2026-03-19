


class bank():
    def __init__(self):
        self.__balance = 10000


    def show_balance(self):
        print(self.__balance)


obj = bank()
obj.show_balance()

#python internally covert it to this
print(obj._bank__balance)
#
# #attribute error in calling it directly
# obj.__balance