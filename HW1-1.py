#Shreyas Keerthi
#I pledge my honor that I have abided by the stevens honor system



from functools import reduce
from math import factorial, sqrt

def add(x,y):
        return x+y
def sqr(x):
    return x**2

    
def taylorApproxE(lastIter):   
    return reduce(add,(list(map(lambda m:1/factorial(m), range(lastIter+1)))))
#compute an approx of e using e^x when x=1
#lastIter represents input which equals iteration after which it should be trunc.


def vectorNorm(vect1):
    return sqrt((reduce(add, map(sqr, vect1))))
#computing the square root of the sum of the squares of the vectors
#vect1 is a list of array of numbers


def arithMean(vect1):  
    return reduce(add,vect1)/len(vect1)
#using the mean of a list by dividing sum of list divided by length

print(taylorApproxE(4))
print(vectorNorm([3,5,11,13]))
print(arithMean([4,1,3,6,12]))
