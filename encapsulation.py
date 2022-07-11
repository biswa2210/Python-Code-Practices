class Phone:
    def __init__(self,a,b,c):
        self.a=a#variable-1
        self._b=b#variable-2
        self.__c=c#variable-3
    def printing(self):#Methods
        print(self.a)
        print(self._b)
        print(self.__c)#PRIVATE
obj=Phone(100,200,300)
print(obj.a)
print(obj._b)
print(obj.__dict__)
print(obj._Phone__c)
obj.printing()