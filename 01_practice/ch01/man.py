# Page 35~36
# 클래스는 인스턴스를 갖는다. 

class Man:
    def __init__(self,name): # Name이라는 인수를 받아 self.name을 초기화
        self.name = name
        print("Initialized")
    
    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()