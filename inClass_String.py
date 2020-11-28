
#This program will work even 
#if the user inputs a string that has numbers or special characters
import re
def main():
    str = input("enter a String: ")
    print("Original String: ", str)
    if str.replace(" ","").isalpha():
        print("\nString is all alphabetical ")
        whiteSpaceRemoved = re.sub("[^0-9a-zA-Z]+" ,'',str)
        vowels(whiteSpaceRemoved)
        consonants(whiteSpaceRemoved)
    else:
         print("\nThe string is NOT alphabetical \nRemoving extra characters...")
         allDigitsRemoved = re.sub('[0-9]','',str)
         print("\n-Digits are removed -> " , allDigitsRemoved)
         allAlphabetical = re.sub("[^0-9a-zA-Z]+" ,'',allDigitsRemoved)
         print("-Special characters and white spaces are removed as well -> ",allAlphabetical)
         vowels(allAlphabetical)
         consonants(allAlphabetical)
        
def vowels(str):   
    count=0
    for letter in str:
        if(letter in 'aAeEiIoOuU'):      
            count+=1
    print("\nThe string has" , count ,"vowels." )


def consonants(str):
      count=0
      for letter in str:
        if(letter not in 'aAeEiIoOuU'):      
            count+=1
      print("The string has" , count ,"consonants." )
   

main()

             