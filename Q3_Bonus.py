#Sara Nersisian
#In Class Activity 1
# 09/03/2020

salary = float(input("Please Input your salary: "))
yearsOfService = int (input('How many years did your work in this company?'))

bonus = (salary * 0.05)

if yearsOfService > 5:
   print("Your bonus amount is $" + format(bonus,'.2f'))
  
else:
   print("No bonus!")
    