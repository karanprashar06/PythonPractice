
#When a child class provides a different implementation of a parent class method.
class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


d = Dog()
d.sound()

c = Cat()
c.sound()