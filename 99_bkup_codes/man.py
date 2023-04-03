#page 35
#class test
#class enables "object-oriented programming"

class Man:
    
    def __init__(self, name):
        self.test = name
        self.test2 = "dear " + name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.test + "!")

    def goodbye(self):
        print("Good-bye " + self.test2 + "!")

m = Man("David")
m.hello()
m.goodbye()

