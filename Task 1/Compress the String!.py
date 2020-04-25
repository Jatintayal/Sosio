from itertools import groupby
# not just any code
for k, g in groupby(input()):
    print("({}, {})".format(len(list(g)), k), end=" ")
