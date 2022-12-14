# an iterators is an object which can be iterated upon which means yo can travers
#kist,s,set,tuple and dictionary are all iterables
#two method to create a iterable
#__iter__():
#__next__():
#iter ,method returns the iter object ,this can be used in i or for statemnets
#next method returns the next value of the object
l=[1,2,3,4,5]
#lazy compution??
'''
in oreder tpo avoid the iteration ,use stop iteration exception
'''
class demo:
    def __init__(self,x):
        self.i=10
        self.n=x
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<=self.n:
            a=self.i
            self.i=self.i+1
            return a
        else:
            raise StopIteration
o=demo(15)
print(list(o))
#a genertor function acts a regular function  but it has one diffrent
#regular function uses the return function statmennet
#genetor function uses the yeild statment
#outcome of genetor function is a iterator-- menass return more than 1 value

def test_seq():
    n=0
    while n<10:
        yield n
        n+=1
for x in test_seq():
    print(x)

#reverse
def reverse_string(s):
    l=len(s)
    for x in range(l-1,-1,-1):
        yield s[x]
for x in reverse_string("Rohan kumar"):
    print(x,end="")
#genetor expression can be used as function argumnets just like list comprehension,
#gentor expression allows you to create a genetor expression quickly, within a few lines of code
    
test_list=[1,3,5,7,9]
#list comprehension
test1=[x**2 for x in test_list]
print(test1)
#genetor expression
test_generator=(x**2 for x in test_list)
print(tuple(test_generator))

