lowerlimit=int(input("Enter the Lower Limit : "))
upperlimit=int(input("Enter the Lower Limit : "))
list=[]
factoriallist=[]
for i in range(lowerlimit,upperlimit+1):
    list.append(i)

for i in list:
    j=0
    mul = 1
    for j in range(1,i+1):
        mul=mul*j;
    factoriallist.append(mul)
dictionary=dict()
def dictconfig(key,diction,value):
    dictionary[key]=value
dictconfig('khubchoto',dictionary,list)
dictconfig('choto',dictionary,factoriallist)
print(dictionary)
print("list of numbers -> {khubchoto} = {choto} <- list of factorials".format(**dictionary))

