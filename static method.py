import string
class big:
    go = 7

    def __init__(self, aname, aage):
        self.name = aname
        self.age = aage

    # @classmethod
    # def change_go(cls, new_go):
    #     cls.go = new_go

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(str):
        return ("THIS IS GOOD "+ str)


biswa = big("Biswa","18+")
print(biswa.name)
print(biswa.age)
romi=big.from_str("Romi-19+")
print(romi.name)
print(romi.age)
print(biswa.printgood(biswa.name))