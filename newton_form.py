from pprint import pprint


"""
Studying for SYDE 211 and SYDE 223 final
"""

measured_points = [(0, 0), (1, 1.6), (2, 3.8), (3, 4.5), (4, 6.3), (5, 9.2), (6, 10.0)]

def batch_gen(data, batch_size):
    for i in range(0, len(data)-batch_size+1):
        yield data[i:i+batch_size]

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

def divided_differences(diffs_table):
    # just playing
    # implementation more closely refects the formula
    prev_diffs = diffs_table[-1]
    if len(prev_diffs) <= 1:
        return None
    else:
        diffs = []
        for (pt_i, pt_i1) in batch_gen(prev_diffs, 2):
            x_i, y_i = pt_i
            x_i1, y_i1 = pt_i1
            dd = (y_i1 - y_i)/(x_i1 - x_i)
            diffs.append((x_i, dd))
        diffs_table.append(diffs)
        divided_differences(x, diffs_table)
        return diffs_table

def interpolate_curve(x, )


pprint(divided_differences([measured_points]))