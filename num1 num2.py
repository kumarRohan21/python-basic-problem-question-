#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell
#
# Created:     16-09-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
num1=int(input("enter the first variables: "))
num2=int(input("enter the second variables: "))
if num1>num2:
    print("num1 is grater than num2")
elif num1<num2:
    print("num1 is less than num2")
elif num1==num2:
    print("num1 is equal to num2")
else:
    print("invalid")