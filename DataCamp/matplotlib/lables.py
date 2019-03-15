#!/usr/bin/env python
import matplotlib.pyplot as plt
import  numpy as np

years = [2001, 2002, 2003, 2004, 2005, 2020]  # this values will be displayed on x-axis
population = [2.38, 2.58, 2.87, 3.25, 4.01, 12.2]  # this values will be displayed on y-axis
pop = [3, 1, 5, 7, 5, 3]  # this list will be used to set radius of displayed dots
np_pop = np.array(pop)
np_pop = np_pop * 5


# Basic scatter plot, log scale
plt.scatter(x = years, y = population, s = np_pop, alpha = 0.8)  # first argument - x-values, second argument - y-values, third argument - diameter of dots? alhpa (fourth element) - change the opacity of dots
plt.xscale('log')  # install parameters to display x axis

plt.grid(True)  # add grid to all axis

plt.text(2005, 4.0, 'India')  # add text to graph. first to arguments - coordinates, third - text,, what will be displayed

# Strings
xlab = 'GDP per Capita [in USD]'  # just string to make name of axis later
ylab = 'Life Expectancy [in years]' # just string to make name of axis later
title = 'World Development in 2007' # just string to make title later

# Definition of tick_val and tick_lab
tick_val = [2000, 2002, 2004, 2006, 2008, 2030]   # just list to make display of axis later
tick_lab = ['2k', '2k02', '2k04', '2k06', '2k08', '2k30']  # just list to make names to displayed names of axis later

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)  # set values and names to certain axis

# Add axis labels
plt.xlabel(xlab)  # set label of x-axis equal string "xlab"
plt.ylabel(ylab)  # set label of y-axis equal string "ylab"



# Add title
plt.title(title)  # set a title of graph equal string "title"

# After customizing, display the plot
plt.show()