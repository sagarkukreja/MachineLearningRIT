# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:22:11 2018

@author: Sagar
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

y = np.arange(-20,20,0.01)
ax.plot(y, norm(0,6).pdf(y),'r-', lw=2, label='norm pdf')