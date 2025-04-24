# **************
# * Name   : Shreyas Keerthi
# * Pledge : I pledge my honor that I have abided by the Stevens Honor System.
# **************

class Rational:
    def __init__(self, n=0, d=1):
        self.numerator = n
        self.denominator = d
        if not self.validate():
            print("Invalid inputs :(")

    def __repr__ (self):
        return "Rational(" + str(self.numerator) \
                + "," + str(self.denominator) + ")"

    def __str__ (self):
       return str(self.numerator) + "/" + str(self.denominator)

    def validate(self):
        return isinstance(self.numerator, int) \
               and isinstance(self.denominator, int) \
               and 0 != self.denominator 

    def isZero(self):
        return 0 == self.numerator

    # TODO
    def simplify(self):
        ''' Convert self into simplest form, i.e.
        2/4 becomes 1/2. Look into GCD!
        Make sure to add calls to simplify
        whenever you make a new rational throughout this code'''
        if self.numerator < self.denominator: 
            minim = self.numerator 
        else: 
            minim = self.denominator 
        for i in range(1, minim+1): 
            if((self.numerator % i == 0) and (self.denominator % i == 0)): 
                gcd = i
        self.numerator=self.numerator//gcd
        self.denominator=self.denominator//gcd
        
              
         

    # TODO
    def invert(self):
        ''' Inverts self (makes it self^-1) '''
        n=self.denominator
        d=self.numerator

        self.numerator=n
        self.denominator=d
      
    def __eq__(self, other):
       return self.numerator * other.denominator \
               == self.denominator * other.numerator

    def __ne__(self, other):
        return self.numerator * other.denominator \
               != self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator \
               < self.denominator * other.numerator
               
    def __le__(self, other):
        return self.numerator * other.denominator \
               <= self.denominator * other.numerator
               
    def __gt__(self, other):
        return self.numerator * other.denominator \
               > self.denominator * other.numerator
               
    def __ge__(self, other):
        return self.numerator * other.denominator \
               >= self.denominator * other.numerator
               
    def __add__(self, other):
        newDenominator = self.denominator*other.denominator
        newNumerator = self.numerator*other.denominator \
                       + self.denominator*other.numerator
        ret = Rational(newNumerator, newDenominator)
        return ret

    def __neg__(self):
        newDenominator = self.denominator
        newNumerator = - self.numerator

        return Rational(newNumerator, newDenominator)

    def __sub__(self, other):
        return self + (-other)

    # TODO
    def __mul__(self, other):
        ''' Returns the product of self and other - SIMPLIFIED
        do not change self or other! '''
        
        newNum = self.numerator*other.numerator
        newDen = self.denominator*other.denominator
        ret=Rational(newNum,newDen)
        ret.simplify()
        
        return ret

    # TODO
    def __truediv__(self, other):
        ''' Returns the result of self/other - simplified
        do not modify self or other ! '''
        num=self.numerator*other.denominator
        den=self.denominator*other.numerator
        ret=Rational(num,den)
        ret.simplify()
        
        return ret

    # TODO
    def __int__(self):
        ''' Returns the integer representation of this rational '''
        return self.numerator//self.denominator

    # Extra Credit: 5 pts
    def continuedFraction(self):
        ''' Returns a string representation of the canonical continued fraction form of self.
        http://mathworld.wolfram.com/SimpleContinuedFraction.html
        5/4 -> [1;4] (since 5/4 = 1 + 1/4)
        33/5 -> [6;1,1,2] (since 33/5 = 6 + 3/5 = 6 + 1/(5/3) = 6 + 1/(1 + 2/3)
                                        = 6 + 1/(1 + 1/(3/2)) = 6 + 1/(1 + 1/(1 + 1/2))
        68/21 -> [3;4,5] (since 68/21 = 3 + 5/21 = 3 + 1/(21/5) = 3 + 1/(4 + 1/5)
        '''
        x=self.numerator
        y=self.denominator
    
        
        
        def helper(x,y):
     
            if(x%y==0):
                f= x//y
            else:
                x-=1
                helper(x,y)

        def helper2(x, y, f):
            rem=x-(f*y)
            nxt=Rational(rem,y)
            nxt.invert()
    
            if (rem!=1):
                x=rem
                y
                helper2(x,y,f)
            else:
                
                
            

        
        
        
            












        
