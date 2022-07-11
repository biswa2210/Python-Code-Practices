numbers=["1","2","3","4","5"]
#for i in range(len(numbers)):
#    numbers[i]=int(numbers[i])
#numbers[2]=numbers[2]+6
#print(numbers[2])
numbers=list(map(int,numbers))
print(list(map(int,numbers)))
print(numbers[3]+8)
sq = lambda a : a*a
cube = lambda a : a*a*a
func=[sq,cube]
for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val)
list1=[1,2,3,4,5,6,7,8,9,10,12]
def is_greater_5(num):
    return num>8   
gr_than_5 = list(filter(is_greater_5,list1))
print(gr_than_5)