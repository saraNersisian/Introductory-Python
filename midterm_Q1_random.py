
import random
def main():
    start = True
    while(start == True):
        num = random.randint(1,101)
        print("Make a guess:")
        guess = int(input(""))
        if(guess > num):
            print("too high, try again.")
            start = False
        elif(guess < num):
            print("too low, try again.")
            start = False
        else: 
            print("Congratulations")
            num = random.randint(1,101)
            start = True
        
main()

