#Sara Nersisian
#In Class Activity 1
#09/03/2020

weight = float(input('Enter your weight (in pounds): '))
height = float(input('Enter your height (in inches): '))

BMI = (weight / (height ** 2) ) * 703

#print('Your weight is ' + weight + 'lbs and your height is ' + height + 'inches.'  )
print('\nYour BMI is' ,format(BMI, '.2f' ))