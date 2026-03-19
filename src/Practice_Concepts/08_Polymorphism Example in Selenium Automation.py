



class Login():
    def login(self):
        print("Welcome logged in")

class Facebook_login(Login):
    def login(self):
        print("Facebook logged in")

class Twitter_login(Login):
    def login(self):
        print("Twitter logged in")


login = Facebook_login()
login.login()
login2 = Twitter_login()
login2.login()
