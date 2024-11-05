""" This module is used to plot the data on a graph"""
from matplotlib import pyplot


def read_data(file_name):
    """
    This scripts reads in data from the file plenty.data
    and plots the points to create a graph.

    """

    # Creates lists for x and y coordinates
    x = []
    y = []
    with open(file_name) as inputfile:
         # Read each line in the input file
        for line in inputfile:
            # Splits line into elements
            elements = line.split()
            # Converts the first element to float and appends it to x
            x.append(float(elements[0]))
             # Converts the rest of the elements to floats and appends to y
            y.append([float(values)for values in elements [1:]])
    return x, y

if __name__ == '__main__':
    # Reads in the data from the file
    x,y = read_data('plenty.data')

# Sets up font properties for the title
csfont = {'fontname': 'Times New Roman'}

# Plots x coordinates against y
pyplot.plot(x,y)

# Makes sure the points start and end at the edges of the graph
pyplot.xlim(min(x), max(x))


# Labels the x and y axes
pyplot.ylabel('Y axis')
pyplot.xlabel('X axis')

# Adds a a grid to the graph
pyplot.grid(linewidth=0.5, axis='both', color = 'grey')
pyplot.title(
    'Assessment1',
    fontsize = 14,
    **csfont
)

pyplot.show()
