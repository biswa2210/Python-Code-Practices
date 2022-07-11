import random
n=random.randint(1,100)
guess=int(input("Guess a number ( range 1 to 100 ) : "))
while n!=guess:
    if guess<100:
            if guess>n:
                print("Guess it lower")
                guess=int(input("Guess a number ( range 1 to 100 ) : "))
            elif guess<n:
                print("Guess it higher")
                guess=int(input("Guess a number ( range 1 to 100 ) : "))
            elif guess==n:
                break
    else:
        print("Invalid Input!!")
        guess = int(input("Guess a number ( range 1 to 100 ) : "))

print("Congo!!! you got it")