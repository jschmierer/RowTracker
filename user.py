from statsdash import StatsDash

class User():

    def __init__(self, u, p, a, n):
        self.user = u
        self.password = p
        self.age = a
        self.name = n
        self.sd = StatsDash()

    def setUser(self, u):
        self.user = u

    def getUser(self):
        return self.user
    
    def setPass(self, p):
        self.password = p

    def getPass(self):
        return self.password

    def setAge(self, a):
        self.age = a

    def getAge(self):
        return self.age

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name
    