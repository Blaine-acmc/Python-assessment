"""
These modules are used to plot data and create maps, as well as add additional
formatting to the output.
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM

def read_data(file_name):
    """
    This script reads coordinate data provided by the City of Edinburgh Council
    and plots them on a map using Cartopy and Matplotlib.

    Functions:
    - read_data(file_name): Parses input data file to extract district
      names and their corresponding coordinates, returning a dictionary
      of district data.

    Usage:
    - Extracts data from 'natural_neighbourhoods.dat' and makes it usable.
    - Run the script to generate a map displaying the districts with
      their boundaries plotted and filled with distinct colours which correspond to a legend.
    """
    # Creates a dictionary for x coordinates, y coordinates, and district names
    map_data = {
        "x_list": [],
        "y_list": [],
        "district_name": ""
    }
    # Creates a dictionary that uses the district name as an identifier for the coordinate block
    stored_data = {}

    # Opens and reads the input file
    with open(file_name) as inputfile:
        # Skips lines that start with metadata
        for line in inputfile:
            line = line.strip()
            line = line.strip("()")
            if line.startswith('#'):
                continue

            # Captures district names that might include spaces or '/'
            if line.replace(' ', '').isalpha() or '/' in line:
                map_data["district_name"] = line

            # Reads data all on one line, converts elements to float, and appends to the x and y lists
            if line.startswith("["):
                line = line.strip("[]")
                elements = line.split("), (")
                for element in elements:
                    coordinates = element.strip("()").split(",")
                    # Ensures the one-line data is read properly
                    try:
                        x = float(coordinates[0].strip())
                        y = float(coordinates[1].strip())
                        map_data["x_list"].append(x)
                        map_data["y_list"].append(y)
                    except ValueError:
                        print(f"Warning: I don't like this data!!! {element}")

            # If a blank line appears, store district data and reset lists
            elif not line:
                district_name = map_data["district_name"]
                # Copies the extracted data
                district_data = {
                    "x_list": map_data["x_list"].copy(),
                    "y_list": map_data["y_list"].copy(),
                    "district_name": district_name
                }
                # Associates the dictionary with the district name
                stored_data[district_name] = district_data
                map_data["x_list"] = []
                map_data["y_list"] = []
                map_data["district_name"] = ""

            # Reads data that is on multiple lines, converts elements to float, and appends to the x and y lists
            else:
                elements = line.split(",")
                if len(elements) == 2:
                    try:
                        x = float(elements[0])
                        y = float(elements[1])
                        map_data["x_list"].append(x)
                        map_data["y_list"].append(y)
                    except ValueError:
                        print(f"Warning: couldn't read multiple lines of data!!! {line}")

    # Returns a dictionary of all processed data
    return stored_data

if __name__ == "__main__":
    coordinates = read_data('natural_neighbourhoods.dat')

    # Sets up the map projection and tile provider
    osgb = ccrs.OSGB()
    tiler = OSM()
    plt.figure(figsize=(6, 6), dpi=150)
    geo_axes = plt.axes(projection=osgb)
    geo_axes.add_image(tiler, 12)
    csfont = {'fontname': 'Times New Roman'}

    # Sets up the title using Times New Roman as the font
    geo_axes.set_title(
        'NATURAL NEIGHBOURHOODS',
        fontsize=14,
        color='forestgreen',
        **csfont
    )
    # Defines map extent showing Edinburgh and uses osgb
    geo_axes.set_extent((308000, 338000, 658000, 682000), crs=osgb)

    # Retrieves a list of colours
    color_list = list(mcolors.CSS4_COLORS.values())

    # Iterates over each district to plot its outline and fill colour
    for i, (district_name, data) in enumerate(coordinates.items()):
        x_list = data['x_list']
        y_list = data['y_list']
        geo_axes.plot(
            x_list,
            y_list,
            linestyle='-',
            linewidth='1',
            color='forestgreen',
            transform=osgb,
        )
        # Fills districts with colours from the retrieved colour list
        geo_axes.fill(
            x_list, y_list,
            color=color_list[i % len(color_list)],
              alpha=0.75,
                label=district_name
        )
        # Configures tick marks and labels using the extent of the map
        geo_axes.set_xticks(range(308000, 339000, 5000))
        geo_axes.set_yticks(range(658000, 683000, 5000))
        geo_axes.set_xticklabels(range(308000, 339000, 5000), rotation=90, fontsize=5)
        geo_axes.set_yticklabels(range(658000, 683000, 5000), fontsize=5)
        # Moves map slightly to the right to make space for the legend
        plt.subplots_adjust(right=0.6)

    # Configures the legend
    plt.legend(
        title='Neighbourhoods',
        loc='best',
        bbox_to_anchor=(1, 1.05),
        fontsize=6,
        title_fontsize=10,
        facecolor='white',
        edgecolor='red',
        ncol=3
    )

    plt.show()
