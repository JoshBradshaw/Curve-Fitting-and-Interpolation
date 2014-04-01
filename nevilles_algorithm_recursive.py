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
    x_i, y_i = pts[i]
    x_j, y_j = pts[j]

    # base case P(x) for a single point is just y
    if i == j:
        return y_i
    else:
        p_left = P(x, pts, (i+1, j))
        p_right = P(x, pts, (i, j-1))
        x_i = pts[i][0]
        x_j = pts[j][0]
        return ((x - x_i)*p_left - (x - x_j)*p_right)/(x_j - x_i)

def divided_differences(pts):
    divided_differences = []
    while len(pts)>1:
        diffs = []
        for (pt_i, pt_i1) in batch_gen(pts, 2):
            x_i, y_i = pt_i
            x_i1, y_i1 = pt_i1
            dd = (y_i1 - y_i)/(x_i1 - x_i)
            diffs.append((x_i, dd))
        divided_differences.append(diffs)
        pts = diffs
    return divided_differences
from pprint import pprint
pprint(divided_differences([(2,-1), (4,4), (5, 8)]))