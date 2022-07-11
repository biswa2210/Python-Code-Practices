class Website:
    def first(self):
        print('freetimelearning.com')
class Second(Website):
    def sec(self):
        print('www.freetimelearning.com')
class Third(Second):
    def final(self):
        print('www.freetimelearn.com')
a=Third()
a.first()
a.sec()
a.final()
