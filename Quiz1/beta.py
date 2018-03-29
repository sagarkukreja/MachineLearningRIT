# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:20:46 2018

@author: Sagar
"""
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1)
a, b = 2, 2
mean, var  = beta.stats(a, b, moments="mv")
x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99,a,b),100)
ax.plot(x, beta.pdf(x, a, b),'r-', lw=5, alpha=0.6, label='beta pdf')
plt.xlabel("x")
plt.ylabel("beta prior")