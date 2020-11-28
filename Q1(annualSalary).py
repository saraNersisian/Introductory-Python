#Sara Nersisian
#In Class Activity 1
# 09/03/2020

#Getting the data from user
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
companyName = input('Enter the company name you wish to work: ')
monthlySalary = float(input('Enetr the monthly salary you wish to earn: '))

annualSalary=(monthlySalary*12)

#Displaying the data
print('\nMy name is ' + name + ', my age is 20')
print('I hope to work for ' + companyName + ' and earn $'+ str(annualSalary) + ' per year.')