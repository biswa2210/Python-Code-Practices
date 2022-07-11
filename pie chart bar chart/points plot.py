# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,2,4])
# plt.show()
a=int(input("HOW MANY POINTS YOU WANT TO PLOT :: "))
list1=[]
list2=[]
for i in range(0,a):
    print("----------------------------->")
    ele1=float(input("x-co-ordinate :: "))
    ele2=float(input("y-co-ordinate :: "))
    print("----------------------------->")
    list1.append(ele1)
    list2.append(ele2)
for (j,k) in zip (list1,list2):
         print("(",j,",",k,")");
import matplotlib.pyplot as plt
plt.plot(list1,list2)
plt.show()