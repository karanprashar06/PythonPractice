


from abc import ABC,abstractmethod
class Login_page(ABC):
    @abstractmethod
    def login(self):
        pass
class Facebook_login(Login_page):
    def login(self):
        print("Facebook login")
class Twitter_login(Login_page):
    def login(self):
        print("Twitter login")

obj2 =Facebook_login()
obj2.login()
obj=Twitter_login()
obj.login()
