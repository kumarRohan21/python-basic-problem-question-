#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Dell
#
# Created:     10-11-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import functools as ft
l=[]
n=int(input("enter the length of list="))
for x in range(n):
    e=int(input("eneter the element for list l="))
    l.append(e)
mx=ft.reduce(lambda a,b: a if a>b else b,l)
mn=ft.reduce(lambda x,y: x if x<y else y,l)
print("maximum=",mx)
print("miniumum=",mn)