#Sara Nersisian
#CS 1260
#Project 1 - Problem 1
#11/14/2020

b = int(input("Enter initial deposited amount: "))
r = int(input("Enter the fixed rate interest: "))
n = int(input("Enter number of years: "))

balance = b * (1 + r/100) ** n
print("\nBalance = $%.2f" %(balance))