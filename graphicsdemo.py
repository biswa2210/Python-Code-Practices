import turtle
import time
#Square Printing
turtle.forward(100)#side
time.sleep(1)#delay
turtle.right(90)#angle
turtle.forward(100)#side
time.sleep(1)#delay
turtle.right(90)#angle
turtle.forward(100)#side
time.sleep(1)#delay
turtle.right(90)#angle
turtle.forward(100)#side

#print rectangle
alex=turtle.Turtle()
for i in [1,2,3,4]:
    if (i==3 or i==1):
      alex.forward(100)
      time.sleep(1)  # delay
      alex.left(90)
    else:
        alex.forward(50)
        time.sleep(1)  # delay
        alex.left(90)
