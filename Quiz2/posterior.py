# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:41:32 2018

@author: Sagar
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

x = np.loadtxt("C:\\Users\\Sagar\\Desktop\\data.txt")
x = np.asarray(x)
y = np.arange(-20,20,0.01)
likelihood_mean =  np.mean(x)
prior_mean = 0
prior_var = 6**2
likelihood_var = 10**2
N = 20
post_var = (likelihood_var*prior_var)/(likelihood_var + (N * prior_var))
post_mean = ((likelihood_var*prior_mean)/(N*prior_var+likelihood_var))+((N*prior_var*likelihood_mean)/(N*prior_var+likelihood_var))
plt.xlabel("data")
ax.plot(y, norm(post_mean,post_var).pdf(y),'r-', lw=2, label='norm pdf')