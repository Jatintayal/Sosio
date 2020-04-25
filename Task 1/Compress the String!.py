from itertools import groupby
# some code
for k, g in groupby(input()):
    print("({}, {})".format(len(list(g)), k), end=" ")
