#!/usr/bin/python

import math

###############################################################################
# Complex Number implementation.
# Each number has a real part, an imaginary part, a magnitude,
# and an indicator of membership in the Mandelbrot set
###############################################################################


class ComplexNumber:

    def __init__(self, real_part, imaginary_part):
        self.re = real_part
        self.im = imaginary_part
        self.mag = math.sqrt(real_part * real_part + imaginary_part * imaginary_part)
        self.is_mandelbrot = None    # Unknown until we run the classification.

    def set(self, real_part, imaginary_part):
        """ Set the values for a complex number, calculate its magnitude.

            Arguments:
            real_part - the real part
            imaginary_part - the imaginary part
        """
        self.re = real_part
        self.im = imaginary_part
        self.mag = math.sqrt(real_part * real_part + imaginary_part * imaginary_part)

    def print_attributes(self):
        """ Print the real and imaginary parts of a complex number,
            along with the magnitude, and whether the number is a
            member of the Mandelbrot set.
        """
        print("Real:", self.re, "Imaginary:", self.im, "Magnitude:", self.mag, "is Mandelbrot:", self.is_mandelbrot)

###############################################################################
# Arithmetic operators for complex numbers: add, subtract, multiply
###############################################################################


class ComplexOperator:

    def add(self, cn1, cn2):
        """ Add two complex numbers, return the sum.

            Arguments:
            cn1 - first addend
            cn2 - second addend
        """
        cn3 = ComplexNumber(cn1.re + cn2.re, cn1.im + cn2.im)
        return cn3

    def subtract(self, cn1, cn2):
        """ Subtract the second complex number from the first, return the difference.

            Arguments:
            cn1 - minuend
            cn2 - subtrahend
        """
        cn3 = ComplexNumber(cn1.re - cn2.re, cn1.im - cn2.im)
        return cn3

    def multiply(self, cn1, cn2):
        """ Multiply two complex numbers, return the product.

            Arguments:
            cn1 - multiplier
            cn2 - multiplicand
        """

        # i^2 = -1
        # (a + xi)(b + yi) = ab-xy + (ay+bx)i
        real = cn1.re * cn2.re - cn1.im * cn2.im
        imag = cn1.re * cn2.im + cn2.re * cn1.im
        cn3 = ComplexNumber(real, imag)
        return cn3

    # TODO: Add divide method.
