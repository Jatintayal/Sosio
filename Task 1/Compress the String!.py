from itertools import groupby
# not just any code, it's a merged code
for k, g in groupby(input()):
    print("({}, {})".format(len(list(g)), k), end=" ")
