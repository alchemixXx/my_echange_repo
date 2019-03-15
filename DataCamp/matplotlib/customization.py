import matplotlib.pyplot as plt
years = [2001, 2002, 2003, 2004, 2005, 2020]
population = [2.38, 2.58, 2.87, 3.25, 4.01, 12.2]

plt.plot(years, population)  # to print dots connected by line
#Customization the graphics
plt.xlabel("years")  # to add name to x-axis
plt.ylabel("population")  # to add name to y-axis
plt.title("World population progression")  # to add a title to the graphs
plt.yticks([0, 2, 4, 6, 8, 10], [0, "2B", "4B", "6B", "8B", "10B"])  # to add the marks and scale of y-axis, we add a list(first argument with the numbers). Second argument should has the same lenght as first and it shows how marks will be written on graph
plt.show()