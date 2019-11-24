#!/usr/bin/python

import ComplexNumbers as CN

###############################################################################
# Utilities for generating and classifying complex numbers.
###############################################################################


class MandelbrotUtilities:

    def __init__(self, real_lower_bound, real_increment, real_steps,
                 imaginary_lower_bound, imaginary_increment, imaginary_steps):
        self.re_lower = real_lower_bound
        self.re_increment = real_increment
        self.re_steps = real_steps
        self.im_lower = imaginary_lower_bound
        self.im_increment = imaginary_increment
        self.im_steps = imaginary_steps
        self.max_iterations = 15
        self.upper_bound = 2.0

    def set_max_iterations(self, max_iterations):
        """ Set the maximum number of iterations through the Mandelbrot computation loop.

            Arguments:
            max_iterations - maximum number of times through the Mandelbrot computation loop.
        """
        self.max_iterations = max_iterations

    def set_upper_bound(self, upper_bound):
        """ Set the magnitude above which a number is not part of the mandelbrot set after
            completing max_iterations of the loop.

            Arguments:
            upper_bound - limit for inclusion in the Mandelbrot set.
        """
        self.upper_bound = upper_bound

    def generate_test_data(self):
        """ Generate a rectangular block of test points on the complex plane.
        """
        test_op = CN.ComplexOperator()
        point = CN.ComplexNumber(self.re_lower, self.im_lower)
        re_start = point.re
        re_delta = CN.ComplexNumber(self.re_increment, 0.0)
        im_delta = CN.ComplexNumber(0.0, self.im_increment)
        complex_list = []

        for y in range(0, self.im_steps):

            for x in range(0, self.re_steps):
                complex_list.append(point)
                point = test_op.add(point, re_delta)

            point = test_op.add(point, im_delta)
            point.re = re_start        # "Carriage return" - reset x position.

        return complex_list

    def classify_mandelbrot(self, c):
        """ Determine if a complex number is a member of the Mandelbrot set.
            True if the result falls within upper_bound after max_iterations.

            Arguments:
            c - the complex number to classify.
        """

        z_next = c
        op = CN.ComplexOperator()

        for i in range(0, self.max_iterations):
            zn_squared = op.multiply(z_next, z_next)
            z_next = op.add(zn_squared, c)

            if z_next.mag > self.upper_bound:
                c.is_mandelbrot = False
                return

        c.is_mandelbrot = True
