#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Dell
#
# Created:     23-11-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
''' method overriding
its an ability of an object oriented programming that allows a child class
to provide a specfic impelation of method that is already provided ,
super class, parent class.
when a method of a sub class have a same name ,same parameter,same type,
as a method in its parent class then to overwite  the method in parent class.
'''
class parent:
    def __init__(self):
        self.a="Inside parent"
    def show(self):
        print("a",self.a)
class child(parent):
    def __init__(self):
        self.a="Inside child"
    def show(self):
        print("a ",self.a)
o1=child()
o2=parent()
o1.show()

o2.show()