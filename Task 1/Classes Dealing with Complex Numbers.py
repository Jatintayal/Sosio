import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        realSum = self.real + no.real
        imaginarySum = self.imaginary + no.imaginary
        return Complex(realSum, imaginarySum)


    def __sub__(self, no):
        realDiff = self.real - no.real
        imaginaryDiff = self.imaginary - no.imaginary
        return Complex(realDiff, imaginaryDiff)

    def __mul__(self, no):
        realProd = self.real*no.real + self.imaginary*no.imaginary*(-1)
        imaginaryProd = self.real*no.imaginary + self.imaginary*no.real
        return Complex(realProd, imaginaryProd)

    def __truediv__(self, no):
        conj = Complex(no.real, no.imaginary*(-1))
        num = self*conj
        denom = no*conj
        realQuo = num.real/denom.real
        imaginaryQuo = num.imaginary/denom.real
        return Complex(realQuo, imaginaryQuo)

    def mod(self):
        m = math.pow(math.pow(self.real,2) + math.pow(self.imaginary,2), 0.5)
        return Complex(m, 0)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')