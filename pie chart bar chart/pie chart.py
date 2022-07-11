import numpy as np
import matplotlib.pyplot as plt
cs=['fuchsia','royalblue','mediumseagreen','salmon','tan','bisque','gold','blue','green','red','cyan','magenta','yellow','orange','darkgreen','lightyellow','teal','aqua','lightblue','skyblue','pink','lightpink']
a=int(input("How many labels are you want to input (Maximum 15 Labels):: "))
list1=[]
size=[]
if a<=15:
    for i in range(0,a):
        ele=input("enter label name :: ")
        ele2=int(input("enter  size (1 to 1000):: "))
        list1.append(ele)
        size.append(ele2)

    plt.pie(size,labels=list1,colors=cs,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.axis('equal')
    plt.show()
else:
    print("INVALID INPUT ! ! !")