#-------------------------------------------------------------------------------
# Name:        module2
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
# filter()
'''filter method filter the given sequence with the help of function that test each elemeent of the sequence it filter to be true ya false'''
# filter(func,seqence)
def func(var):
    vowel=["a","e","o","i","u"]
    if var in vowel:
        return True
    else:
        return False
l=["g","e","m","a","k","p","u","i","y"]
result=filter(func,l)
print("list of vowels",list(result))