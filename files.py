# Sara Nersisian
# In class activity on files

import sys
def main():
    filename = input("Enter a file name: ")
   #making sure such a file exists 
    try:
        file = open(filename)
    except FileNotFoundError:
        print("The file does not exist")
        sys.exit()
    except:
        print("Something went wrong")
        sys.exit()
    #now if the file exists, start the program
    print("Opening file  \'" + filename + "\'")
    print("Reading file  \'" + filename + "\'")
    file = open(filename,'r')
    count = 0
    print()
    for line in file:
        count += 1
        print("{}:{}".format(count, line.strip()))
    print("\nClosing file \'" + filename + "\'")
    file.close()
main()