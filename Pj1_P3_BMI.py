#Sara Nersisian
#CS 1260
#Project 1 - Problem 3
#11/14/2020
import sys
def main():
    print("\n   *********** BMI Calculator ***********")
    again = 'y'
    while again == 'y':
        print("\nPLease make a selection on the prefered units: \n 1) Metric (kg/m) \n 2) English (lb/in)" , end="")
        choice = int(input("Your choice: "))               
                           
        if choice == 1 or choice ==2:
            if choice == 1:
                weight = getWeight()
                height = getHeight()
                BMI = weight / (height ** 2)
                status = BMI_table(BMI)    
            elif choice == 2:
               weight = getWeight()
               height = getHeight()
               BMI = ( weight / (height ** 2) ) * 703
               status = BMI_table(BMI)  
            print("\n<< ------------ RESULTS -------------- >>")            
            print("Your BMI is %.2f" %BMI)   
            print("Based on your BMI your body status is \"%s\"" %status)
        else: 
            print("Invalid selection! Try again")
            sys.exit()
        again = input("\nContinue (y/n)? ")
        if(again != 'y'  or again != 'Y' or again != 'n' or again != 'N' ):
            print("Invalid Choice!")
            
    print("Exiting the program...")
       
#Fuctions
def getWeight():
    #Error: Invalid data format validation
    try:
        weight = float(input("Please enter your weight : "))
    except ValueError: 
        print("The input was not valid format (enter int/float)")
        sys.exit()
    #Error: Invalid data value validation
    if weight<=0:
        print("Invalid Weight! Weight cannot be zero or negative")
        sys.exit()
    return weight
       
def getHeight():         
    #Error: Invalid data format validation
    try:
        height = float(input("Please enter your height : "))
    except ValueError: 
        print("The input was not valid format (enter int/float)")
        sys.exit()
    #Error: Invalid data value validation
    if height <=0:
        print("Invalid Height! height cannot be zero or negative")
        sys.exit()
    return height
        
def BMI_table(BMI):
    if BMI>0 and BMI <= 24:
        status = "Normal"
    elif BMI >= 25 and BMI <= 29:
        status = "Overweight"
    elif BMI >= 30 and BMI <= 39:
        status = "Obese"
    elif BMI >40:
        status = "Extreme obesity"
    else:
        print("The staus is UNAVAILABLE, please try again")
    return status

main()