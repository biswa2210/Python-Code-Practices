class mitti:
    mittimitti=45
    def __init__(self,aname,aage):
        self.name=aname
        self.age=aage
    def mittifunc(self):
        return f"puku puku {self.name}"
biswa=mitti("Biswa","18")
print(biswa.name)
print(biswa.age)
mitti.mittimitti=56
print(biswa.mittimitti)
print(biswa.mittifunc())