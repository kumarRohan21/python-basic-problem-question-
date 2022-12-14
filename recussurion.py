#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell
#
# Created:     12-10-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# recurssion using stag
def sum(x):
    if x==0:
        return 0
    else:
         return x+sum(x-1)

n=int(input("enter the value of all the requried="))
r=sum(n)
print("tota sum=",r)