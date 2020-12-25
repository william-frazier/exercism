import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real_portion = self.real * other.real - self.imaginary * other.imaginary
        imaginary_portion = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_portion, imaginary_portion)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def __truediv__(self, other):
        real_portion = (self.real * other.real + self.imaginary * other.imaginary) / (other.real**2 + other.imaginary**2)
        imaginary_portion = (self.imaginary * other.real - self.real * other.imaginary) / (other.real**2 + other.imaginary**2)
        return ComplexNumber(real_portion, imaginary_portion)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        first = math.e ** self.real
        return ComplexNumber(first * math.cos(self.imaginary), math.sin(self.imaginary))
