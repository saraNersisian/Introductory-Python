def is_prime(num):
    for number in range(2,num-1):
        if(num%number == 0):
            return False           
        else:
            return True
        
def main():
    for num in range(2,101):
       if is_prime(num) == True:
           print(num)
main()