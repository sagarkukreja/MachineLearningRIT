# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:20:46 2018

@author: Sagar
"""
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1)
# posterior for beta is beta only
#a is 2+ 4 now as 2 is fictious number of head and 4 is real number of heads
#b is 2+1 now as 2 is fictious number of tails and 1 is real number of tails
a, b = 6, 3
mean, var  = beta.stats(a, b, moments="mv")
x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99,a,b),100)
ax.plot(x, beta.pdf(x, a, b),'r-', lw=5, alpha=0.6, label='beta pdf')
plt.xlabel("x")
plt.ylabel("posterior distribution")
print(mean)