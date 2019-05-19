#!/usr/bin/python

import math

###############################################################################
# Complex Number implementation.
# Each number has a real part, an imaginary part, a magnitude,
# and an indicator of membership in the Mandelbrot set
###############################################################################

class ComplexNumber:

    def __init__(self, realPart, imaginaryPart):
        self.re = realPart
        self.im = imaginaryPart
        self.mag = math.sqrt(realPart * realPart + imaginaryPart * imaginaryPart)
        self.isMandelbrot = None    #Unknown until we run the classification.

    def Set(self, realPart, imaginaryPart):
        self.re = realPart
        self.im = imaginaryPart
        self.mag = math.sqrt(realPart * realPart + imaginaryPart * imaginaryPart)

    def PrintAttributes(self):
        print ("Real: {re}, Imaginary: {im}, magnitude: {mag}, isMandelbrot: {mand}"
              .format(re = self.re, im = self.im, mag = self.mag, mand = self.isMandelbrot))

###############################################################################
# Arithmetic operators for complex numbers: add, subtract, multiply
###############################################################################

class ComplexOperator:

    def Add(self, cn1, cn2):
        cn3 = ComplexNumber(cn1.re + cn2.re, cn1.im + cn2.im)
        return cn3

    def Subtract(self, cn1, cn2):
        cn3 = ComplexNumber(cn1.re - cn2.re, cn1.im - cn2.im)
        return cn3

    # i^2 = -1
    # (a + xi)(b + yi) = ab-xy + (ay+bx)i

    def Multiply(self, cn1, cn2):
        real = cn1.re * cn2.re - cn1.im * cn2.im
        imag = cn1.re * cn2.im + cn2.re * cn1.im
        cn3 = ComplexNumber(real, imag)
        return cn3
