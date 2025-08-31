import random

//to Generate random number between 1 to 100
n=random.randint(1,100)

a=-1
guesses=0

while(a!=n):
    guesses+=1
    a=int(input("Guess a number: "))    

    if(a>n):
        print("Lower Number please!!")
    else:
        print("Higher Number please!!")


print(f'You have correctly gussed the number {n} in {guesses} attempt')
