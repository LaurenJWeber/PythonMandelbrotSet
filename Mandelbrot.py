#!/usr/bin/python

###############################################################################
# Plot the Mandelbrot set.
###############################################################################

import ComplexNumbers as cn
import ComplexUtilities as cu
import matplotlib.pyplot as plotter
import argparse
import json

###############################################################################
# Main function
###############################################################################

def main():

    parser = argparse.ArgumentParser(description="Plot the Mandelbrot set")
    parser.add_argument("JsonConfig", help="Path to Json configuration file")
    args = parser.parse_args()
    print "==>Initializing..."

    with open(args.JsonConfig) as json_data:
        configuration = json.load(json_data)

    realStart = configuration["realStart"]
    realDelta = configuration["realDelta"]
    realSteps = configuration["realSteps"]
    imaginaryStart = configuration["imaginaryStart"]
    imaginaryDelta = configuration["imaginaryDelta"]
    imaginarySteps = configuration["imaginarySteps"]
    upperBound = configuration["upperBound"]
    maxIterations = configuration["maxIterations"]

    print "==>Generating test data..."
    myCU = cu.ComplexUtilities(realStart, realDelta, realSteps,
            imaginaryStart, imaginaryDelta, imaginarySteps)
    testPoints = myCU.GenerateTestData()
    mandelbrotXValues = []
    mandelbrotYValues = []
    pointCounter = 0
    printStatusIncrement = 10000
    print "==>Classifying data..."

    for testPoint in testPoints:
        myCU.ClassifyMandelbrot(testPoint, upperBound, maxIterations)

        if testPoint.isMandelbrot:
            mandelbrotXValues.append(testPoint.re)
            mandelbrotYValues.append(testPoint.im)

        pointCounter += 1

        if pointCounter % printStatusIncrement == 0:
            print "Processed {pts} points".format(pts = pointCounter)

    print "==>Plotting data..."
    plotter.scatter(mandelbrotXValues, mandelbrotYValues, marker = '.', s = 1)
    plotter.xlabel('Re')
    plotter.ylabel('Im')
    plotter.title('Mandelbrot Set: ' + str(pointCounter) + " test points")
    plotter.show()

###############################################################################
# Begin!
###############################################################################

if __name__ == "__main__":
    main()
