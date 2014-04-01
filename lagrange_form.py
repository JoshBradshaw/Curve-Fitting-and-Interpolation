from __future__ import division
from math import *

# to add: theoretical error bound with sympy

measured_points = [(0, 0), (pi/4, 1/sqrt(2)), (pi/2, 1)]


def lagrange_polynomial(interpolating_x, measured_points):
    """
    Naive approach that runs in O(n^2)

    x_j is the jth value of x
    interpolating_x is the value of x we are approximating
    """
    interpolated_value = 0
    # build difference of x values term
    for x_j, y_j in measured_points:    
        Lnj_x = 1
        for x_i, y_i in measured_points:
            if not x_i == x_j:
                Lnj_x *= (interpolating_x - x_i)/(x_j-x_i)
            else:
                Lnj_x *= y_i
        interpolated_value += Lnj_x
    return interpolated_value

print lagrange_polynomial(pi/3, measured_points)

import matplotlib.pyplot as plt
import numpy as np
x_vals = np.arange(0, pi/2, 0.01)
print x_vals

sin_y_vals = []
approx_vals = []
for x in x_vals:
    sin_y_vals.append(sin(x))
    approx_vals.append(lagrange_polynomial(x, measured_points))

plt.plot(x_vals, sin_y_vals, 'ro', x_vals, approx_vals, 'r--')
plt.axis([0, 6, 0, 20])
plt.show()