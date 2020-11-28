#Sara Nersisian
#CS 1260
#Project 1 - Problem 2
#11/14/2020

import math
print("\n*** Quadretic Equation Solver ***")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

determinant = (b ** 2) - 4 * a * c

if determinant > 0:
    x1 = (-1 * b + math.sqrt(determinant)) / (2 * a)
    x2 = (-1 * b - math.sqrt(determinant)) / (2 * a)
    print("\nThe two real roots are %.2f and %.2f" %(x1,x2))
elif determinant == 0:
    x = (-1 * b ) / (2 * a)
    print("\nThe Only real root is %.2f" %(x))
else:
    print("\nNo real roots! ")
    
    
    
    
