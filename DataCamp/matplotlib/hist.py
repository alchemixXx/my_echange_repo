#!/usr/bin/env python

import matplotlib.pyplot as plt

# help(plt.hist)
x = [1,2,3,5,7]

plt.hist(x, bins = 3)  # x - where take a data; bins - how many bins you need
plt.show()