#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dell
#
# Created:     14-11-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class volume:
    def __init__(self,r,h):
        self.radius=r
        self.height=h
        self.sphere=(1.33)*3.14*(self.radius**3)
        self.cone=(0.33)*3.14*(self.radius*self.radius*self.height)
        self.cyl=3.14*(self.radius*self.radius*self.height)
    def display(self):
        print("volume of shphere=",self.sphere)
        print("volume of cone=",self.cone)
        print("volume of cyliner=",self.cyl)
a=volume(3.8,4.9)
a.display()
print()
b=volume(5.8,7.9)
b.display()