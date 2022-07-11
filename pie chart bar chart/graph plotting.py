import matplotlib.pyplot as plt
import numpy
print("\nTWO GRAPHS  PLOT SIMULTANEOUSLY----->\n")
a=int(input("HOW MANY POINTS YOU WANT TO PLOT FOR 1st GRAPH :: "))
list1=[]
list2=[]
for i in range(0,a):
    print("----------------------------->")
    ele1=float(input("x-co-ordinate :: "))
    ele2=float(input("y-co-ordinate :: "))
    print("----------------------------->")
    list1.append(ele1)
    list2.append(ele2)
plt.plot(list1,list2, label= "line 1")
plt.scatter(list1,list2)
plt.grid(True)
a=int(input("HOW MANY POINTS YOU WANT TO PLOT FOR 2nd GRAPH :: "))
list3=[]
list4=[]
for i in range(0,a):
    print("----------------------------->")
    ele12=float(input("x-co-ordinate :: "))
    ele22=float(input("y-co-ordinate :: "))
    print("----------------------------->")
    list3.append(ele12)
    list4.append(ele22)
plt.plot(list3,list4, label= "line 2")
plt.scatter(list3,list4)
plt.grid(True)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two lines on a graph !')
plt.legend()
print("\nPOINTS FOR 1ST LINE............>\n")
for (j,k) in zip (list1,list2):
         print("(",j,",",k,")");
         print("\n...........................................\n")
print("\nPOINTS FOR 2ND LINE............>\n")
for (m, n) in zip(list3, list4):
             print("(",m, ",", n, ")");
             print("\n...........................................\n")
plt.show()