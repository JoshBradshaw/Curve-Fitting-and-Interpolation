from __future__ import division
measured_points = [(0, 0), (1, 1.6), (2, 3.8), (3, 4.5), (4, 6.3), (5, 9.2), (6, 10.0)]


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

print lagrange_polynomial(interpolating_x, measured_points)