#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dell
#
# Created:     30-08-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#----------------------------------------------------------------------------
first = input("enter the first number :")
operater =input("enter the operater (+,-,/,*,%,//,)")
second =input("enter the second bumber :")
first = int(first)
second =int(second)
if operater=="+":
    print(first+second)
elif operater=="-":
    print(first-second)
elif operater=="/":
    print(first/second)
elif  operater=="*":
    print(first*second)
elif  operater=="%":
    print(first%second)
elif operater=="//":
    print(first//second)
else:
    print(invalid)