# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 19:08:33 2018

@author: Sagar
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0,1,0.01)
p = 4 #number of heads
q = 1 #number of tails
j = []
#calculating the likelihood.. theta^#heads*(1-theta)^#tails
for i in range(len(y)):
    t = pow(y[i],p)
    l = pow((1-y[i]),q)
    r = t*l
    j.append(r)
plt.plot(y,j)
plt.xlabel("x")
plt.ylabel("likelihood distribution")
plt.show()