#!/usr/bin/python

###############################################################################
# Plot the Mandelbrot set.
###############################################################################

from ComplexUtilities import MandelbrotUtilities as Utils
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
    print("==>Initializing...")

    with open(args.JsonConfig, "r") as json_data:
        configuration = json.load(json_data)

    real_start = configuration["real_start"]
    real_delta = configuration["real_delta"]
    real_steps = configuration["real_steps"]
    imaginary_start = configuration["imaginary_start"]
    imaginary_delta = configuration["imaginary_delta"]
    imaginary_steps = configuration["imaginary_steps"]
    upper_bound = configuration["upper_bound"]
    max_iterations = configuration["max_iterations"]

    print("==>Generating test data...")
    utility = Utils(real_start, real_delta, real_steps,
                    imaginary_start, imaginary_delta, imaginary_steps)
    test_points = utility.generate_test_data()
    utility.set_max_iterations(max_iterations)
    utility.set_upper_bound(upper_bound)
    mandelbrot_x_values = []
    mandelbrot_y_values = []
    point_counter = 0
    print_status_increment = 10000
    print("==>Classifying data...")

    for test_point in test_points:
        utility.classify_mandelbrot(test_point)

        if test_point.is_mandelbrot:
            mandelbrot_x_values.append(test_point.re)
            mandelbrot_y_values.append(test_point.im)

        point_counter += 1

        if point_counter % print_status_increment == 0:
            print("Processed", point_counter, "points.")

    print("==>Plotting data...")
    plotter.scatter(mandelbrot_x_values, mandelbrot_y_values, marker='.', s=1)
    plotter.xlabel('Re')
    plotter.ylabel('Im')
    plotter.title('Mandelbrot Set: ' + str(point_counter) + " test points")
    plotter.show()

###############################################################################
# Begin!
###############################################################################


if __name__ == "__main__":
    main()
