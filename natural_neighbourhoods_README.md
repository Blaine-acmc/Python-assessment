# **Python Programming Assignment Task 2**

This project creates a map of Edinburgh using the Natural Neighbourhoods data provided by the City of Edinburgh Council. 
The script extracts the coordinate data of the district polygons and then plots them on a map using Cartopy and Matplotlib. 
The districts are all assigned a different colour which corresponds to a legend.

### **Features:**

- Parses the input data into a useable format for creating a map.
- Plots district boundaries each with a unique colour associated with it.
- Creates a visually appealing map of Edinburgh's districts complete with a legend.

### **Installations:**

- **Matplotlib:** plots data 
- **Cartopy:** creates map

### **Optional modules:**

- matplotlib.colors for larger selection of colours
- cartopy.io.img_tiles/OSM for OSM map as background; can use coastlines as alternative

### **Data file:**

- [natural_neighbourhoods.dat] data/natural_neighbourhoods.dat

### **Map Configuration:**

- Projection: OSGB (Ordnance Survey National Grid).
- Extent: 308000, 338000, 658000, 682000 (Edinburgh).
- Visuals: Uses CSS4 colour palette and Times New Roman font for the title.