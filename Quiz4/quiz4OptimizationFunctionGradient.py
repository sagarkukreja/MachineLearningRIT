# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:30:42 2018
optimization of function f = 100*(x2-x1)^2 + (1-x1)^2 
using gradient descent
@author: Sagar
"""

import numpy as np
from sympy import *

x1 = Symbol("x1")
x2 = Symbol("x2")

f = 100*x1**4 + x1**2 + 100*x2**2 - 200*x2*x1**2 - 2*x1 + 1
dfdx1 = f.diff(x1) # first  derivative with respect to x1
dfdx2 = f.diff(x2)  # first derivative with respect to x2
#print(dfdx1)
#print(dfdx2)

# Gradient
grad = [dfdx1,dfdx2]

# Data

theta1 = 2 # initial x1
theta2 = 5 # initial x2
alpha = 0.001 # learning rate
iterations = 0
precision = 1/1000000
maxIterations = 1000

# gradient descent algorithm
while True:
    temptheta1 = theta1 - alpha*N(dfdx1.subs(x1,theta1).subs(x2,theta2)).evalf()
    temptheta2 = theta2 - alpha*N(dfdx2.subs(x2,theta2).subs(x1,theta1)).evalf()
    
    iterations += 1
    
    if iterations > maxIterations:
        break
    
    # convergence condition
    if abs(temptheta1-theta1) < precision and abs(temptheta2-theta2) < precision :
        break
    
    
    theta1 = temptheta1
    theta2 = temptheta2

print("Gradient descent: ")
print("x1 ", theta1)
print("x2 ", theta2)