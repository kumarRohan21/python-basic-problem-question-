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
def abc(n):
    return lambda x: x*n
ret= abc(7)
print("multiplication=",ret(6))
s=lambda x:x*x if x>0 else none
print(s(8))
f=lambda x:print("even")if x%2==0 else print("odd")
a=int(input("enter the value="))
f(a)
f=lambda a,b,c: if a>b elif b>c else c
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
print("largest b/w three=",f(a,b,c))