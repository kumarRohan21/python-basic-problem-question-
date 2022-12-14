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
#reduce function is defined in labrary tools
'''the working of reduce funtion
at first two steps the sequnce are fixed
import
apply the same fucntion the previously attend result  and the number just succeding the second element
and the result is obtained
strp2=== the process is continue the no more
the final result is obtained and filter in a concole
wirte a program in oyt'''
import functools as ft
l=[2,4,6,8,10,20,30,40,60]
print(ft.reduce(lambda x,y:x+y,l))
