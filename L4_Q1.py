

import random
def main():
    num1 = random.randint(100,500)
    print("num1: ", num1)
    num2 = random.randint(100,500)
    print("num2: ", num2)
    print("Enter the result of the addition: ")
    addition = int(input(" "))
    if(addition == num1 + num2):
        print("Congratulations!")
    else:
        print("Wrong Answer!")
main()