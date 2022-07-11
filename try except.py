print("enter 1st number :: ")
num1=input()
print("enter 2nd number ::  ")
num2=input()
try:
    print("SUM IS :: ",int(num1)+int(num2))
except Exception as e:
    print(e)
print("This is line so important")