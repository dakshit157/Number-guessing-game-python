import random

n = random.randint(1,50)

a = -1
guesses = 1



while (n != a):
    a = int(input("Choose a Number Between(1 to 50) : "))

    if(a<n) :
        print("Choose Higher Number!!")
        guesses+=1
        
    elif(a>n) :
        print("Choose Lower Number!!")
        guesses+=1

print(f"You Choosed Currect Number in {guesses} attempts!!!")

