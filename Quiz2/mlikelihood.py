# -*- coding: utf-8 -*-
"""

"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

x = np.loadtxt("C:\\Users\\Sagar\\Desktop\\data.txt")
x = np.asarray(x)
y = np.arange(-20,20,0.01)
mean = np.mean(x)
plt.xlabel("data")
ax.plot(y, norm(mean,10).pdf(y),'r-', lw=2, label='norm pdf')