

class employee():
        def __init__(self):
            self._salary = 100

class manager(employee):
    def show_salary(self):
        print(self._salary)

m= manager()
m.show_salary()