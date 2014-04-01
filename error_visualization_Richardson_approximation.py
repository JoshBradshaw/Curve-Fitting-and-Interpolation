from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import math

domain = (1.5, 2.5)
f = lambda x: math.log(x)
epsilon = 0.05

def evenly_spaced_x_values(test_domian, spacing):
    l, r = test_domian
    return np.arange(l, r, spacing)

def derivative_approx(f, x, e):
    # using the formula 
    # De = De/2 + O(e^3)
    De = (f(x + 2*e) - f(x-e))/(3*e)
    De_2 = (f(x+e) - f(x-e/2))/((3/2) * e)
    return 2*De_2 - De


x_vals = evenly_spaced_x_values(domain, 0.01)
exact = [1/x for x in x_vals]
approx_vals = [derivative_approx(f, x, epsilon) for x in x_vals]


plt.plot(x_vals, exact, 'go', x_vals, approx_vals, 'r--')
plt.axis([0, 6, 0, 20])
plt.show()