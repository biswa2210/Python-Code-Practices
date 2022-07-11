#faulty operations 45*3=555,56+9=77,56/6=555
n1=int(input("enter your 1st number : "))
n2=int(input("enter your 2nd number : "))
print("1--->'+'\n2--->'-'\n3--->'*'\n4--->'/'\n5--->'%")
choice=input("enter your choice ")
if choice=="1":
     if (n1==56 and n2==9) or (n1==9 and n2==56):
              print("56+9=77")
     else:
              print(n1+n2)
elif choice=="2":
   print(n1-n2)
elif choice=="3":
     if (n1 == 45 and n2 == 3) or (n1 == 3 and n2 == 45):
        print("45*3=555")
     else:
        print(n1*n2)


elif choice=="4":
  if n1 == 56:
     if n2 == 6:
                  print("56/6=555")
     else:
                  print(n1 / n2)
  else:
                  print(n1 / n2)
elif choice=="5":
      print(n1 % n2)
else:
 print("INVALID CHOICE INPUT")
