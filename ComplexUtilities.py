#!/usr/bin/python

import ComplexNumbers as cn

###############################################################################
# Utilities for generating and classifying complex numbers.
###############################################################################

class ComplexUtilities:

    def __init__(self, realLowerBound, realIncrement, realSteps,
                 imaginaryLowerBound, imaginaryIncrement, imaginarySteps):
        self.reLower = realLowerBound
        self.reIncrement = realIncrement
        self.reSteps = realSteps
        self.imLower = imaginaryLowerBound
        self.imIncrement = imaginaryIncrement
        self.imSteps = imaginarySteps

    ###########################################################################
    # Generate a rectangular block of test points on the complex plane.
    ###########################################################################

    def GenerateTestData(self):

        testCO = cn.ComplexOperator()
        point = cn.ComplexNumber(self.reLower, self.imLower)
        reStart = point.re
        reDelta = cn.ComplexNumber(self.reIncrement, 0.0)
        imDelta = cn.ComplexNumber(0.0, self.imIncrement)
        complexList = []

        for y in xrange(0, self.imSteps):

            for x in xrange(0, self.reSteps):
                complexList.append(point)
                point = testCO.Add(point, reDelta)

            point = testCO.Add(point, imDelta)
            point.re = reStart        # "Carriage return" - reset x position.

        return complexList

    ###########################################################################
    # Determine if a complex number is a member of the Mandelbrot set.
    # True if the result falls within upperBound after maxIterations.
    ###########################################################################

    def ClassifyMandelbrot(self, c, upperBound, maxIterations):

        zNext = c
        mandelbrotCO = cn.ComplexOperator()

        for i in xrange(0, maxIterations):
            znSquared = mandelbrotCO.Multiply(zNext, zNext)
            zNext = mandelbrotCO.Add(znSquared, c)

            if zNext.mag > upperBound:
                c.isMandelbrot = False
                return

        c.isMandelbrot = True
