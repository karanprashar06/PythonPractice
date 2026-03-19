


class Calculator:
#Python does not support traditional overloading, but it can be achieved using default arguments.
    def add(self, a, b, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(2,3))
print(obj.add(2,3,5))