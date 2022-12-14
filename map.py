#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell
#
# Created:     09-11-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
'''after applying  given function to each items of a given itterable thast etc
function parameter is a function to which map passes each eelement of a given itteriable
#2 = iiterable is a object which is to be map'''
#note ==  you can pass one or more itteriable to a funtion
'''return of the map function
after applying a given  function to each item to the itterable
ex-'''
def addition(n):
    return n+n
numbers=(10,20,30,40,50)
result=map(lambda x:x+x,numbers)
print(list(result))
l=[2,5,4,6]
sl=map(lambda x:x**2,l)
print("squree list=",list(sl))