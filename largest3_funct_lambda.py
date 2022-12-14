#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell
#
# Created:     06-10-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
f=lambda a,b,c: a if(a>b and a>c) else (b if(b>c) else c)
x=int(input("enetr the number="))
y=int(input("enetr the number="))
z=int(input("enetr the number="))
print("largest b/w three=",f(x,y,z))