from __future__ import division

measured_points = [(0, 0), (1, 1.6), (2, 3.8), (3, 4.5), (4, 6.3), (5, 9.2), (6, 10.0)]

def P(x, pts, point_range):
    """
    returns polynomial approximation based on Neville's algorithm
    """
    # this recursive implementation is intractable because it repeats
    # so much work. It could be fixed by keeping cache of intermediate
    # values in a hash table

    i, j = point_range
    x_i = pts[i][0]
    y_i = pts[i][1]
    x_j = pts[j][0]
    y_j = pts[j][1]

    # base case P(x) for a single point is just y
    if i==j:
        return y_i
    else:
        p_left = P(x, pts, (i+1, j))
        p_right = P(x, pts, (i, j-1))
        x_i = pts[i][0]
        x_j = pts[j][0]
        return ((x - x_i)*p_left - (x - x_j)*p_right)/(x_j - x_i)

print P(1.5, measured_points, (0, 6))