# Sara Nersisian
# CS 1260 - In class activity 2
# 09/15/2020


series = 0
sumOfSeries = 0
count = 0

print("\nEnter negative number to stop.")
while series >= 0 :
    series = int(input("Please enter positive integers: "))
    if series < 0:
        print("\nYou have stopped entering.")
        break
    sumOfSeries += series
    count+=1

print('\nSumOfSeries =', sumOfSeries)
print('count = ', count)