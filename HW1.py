#Shreyas Keerthi
#I pledge my honor that I have abided by the stevens honor system



from functools import reduce
from math import factorial, sqrt
def add(x,y):
        return x+y

    
def taylorApproxE(lastIter):   
    return reduce(add,(list(map(lambda m:1/factorial(m), range(t+1)))))
            
def vectorNorm(vect1):
    def square(x):
        return x**2
   
    return sqrt((reduce(add, map(square, vect1))))

def arithMean(vect1):
    divs=list(map(lambda x:x/len(vect1),vect1))
    return reduce(add,divs)
