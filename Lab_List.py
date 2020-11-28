

num=[]
print('enter 20 numbers: ')

i=1;
while i <= 20:
    add=int(input())
    num.append(add)
    i+=1

print('The lowest number is: ', min(num))
print('The Highest number is: ', max(num))
print('The Total of the numbers is: ', sum(num))
print('The Avarage of the numbers is: ', sum(num)/20)