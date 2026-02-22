

class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fullname(self):
        return self.name + " " + str(self.age)

obj_ref = Person("Karan", 18)
print(obj_ref.fullname())