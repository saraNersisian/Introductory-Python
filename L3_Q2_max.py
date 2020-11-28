def find_max(num1, num2):
    if(num1>num2):
        max=num1
    else:
        max=num2
        
    return max;



num1=float(input("num1: "))
num2=float(input("num2: "))
num3=float(input("num3: "))
num4=float(input("num4: "))

max1=find_max(num1,num2)
max2=find_max(num3,num4)

sum=max1+max2
print("\nsum= ", sum)