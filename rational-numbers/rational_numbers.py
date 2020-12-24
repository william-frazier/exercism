from __future__ import division
from math import gcd

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        self.reduce()
        other.reduce()
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        denom = self.denom * other.denom
        output = Rational(numer,denom)
        output.reduce()
        return output

    def __sub__(self, other):
        numer = (self.numer * other.denom) - (other.numer * self.denom)
        denom = self.denom * other.denom
        output = Rational(numer,denom)
        output.reduce()
        return output

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        output = Rational(numer,denom)
        output.reduce()
        return output

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        output = Rational(numer,denom)
        output.reduce()
        return output
        

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        output = Rational(numer,denom)
        output.reduce()
        return output        

    def __pow__(self, power):
        numer = pow(self.numer, power)
        denom = pow(self.denom, power)
        output = Rational(numer,denom)
        output.reduce()
        return output

    def __rpow__(self, base):
        return pow(base, self.numer/self.denom)

    def reduce(self):
        divisor = gcd(self.numer, self.denom)
        self.numer = self.numer // divisor
        self.denom = self.denom // divisor
        if self.denom < 0 and self.numer < 0:
            self.denom = abs(self.denom)
            self.numer = abs(self.numer)
        if self.denom < 0 and self.numer >= 0:
            self.numer = -1 * self.numer
            self.denom = abs(self.denom)
        