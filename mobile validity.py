#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dell
#
# Created:     22-09-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
m=int(input("enter the mobile number="))
m=str(m)
length=len(m)
if length == 10:
    if m.isdigit()==True:
        print(m,"is valid mobile number")
    else:
        print(m,"is not valid mobile number")
else:
    print("mobile number should contain 10 digit only")