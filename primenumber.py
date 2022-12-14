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
dc=0
n =int(input())
for x in range (1,n+1):

    if n%x==0:
        dc=dc+1
if dc==2:
    print(n,"is the prime")
else:
    print(n,"is not prime because divison count =",dc)
