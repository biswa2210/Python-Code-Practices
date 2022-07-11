import matplotlib.pyplot as plt
import numpy as np
print("\nHELLO SIR I AM GRAPHER \nI PLOT GRAPH OR ONE CURVE THROUGH POINTS [(X,Y) FORMAT]\nPLEASE GIVE ME POINTS FOR PLOTING----->\n")
t=input("Print the title of the graph :: ")
xl=input("Enter name of x-axis : ")
yl=input("Enter name of y-axis : ")
a=int(input("HOW MANY POINTS YOU WANT TO PLOT FOR YOUR GRAPH :: "))
list1=[]
list2=[]
for i in range(0,a):
    print("----------------------------->")
    ele1=float(input("x-co-ordinate :: "))
    ele2=float(input("y-co-ordinate :: "))
    print("----------------------------->")
    list1.append(ele1)
    list2.append(ele2)
plt.plot(list1,list2, label="Your Curve")
plt.legend(loc="best")
plt.scatter(list1,list2)
plt.grid(True)
plt.xlabel(xl)
plt.ylabel(yl)
plt.title(t)
print("\nPOINTS FOR 1ST LINE............>\n")
for (j,k) in zip (list1,list2):
         print("(",j,",",k,"),");
print("\n...........................................\n")
slope, intercept = np.polyfit(list1, list2, 1)
print("SLOPE OF YOUR GRAPH :: ",slope)
fname=input("Enter your file name to save the graph :: ")
plt.savefig(fname)
print("ok bye .....created by Biswa..........")
plt.show()


