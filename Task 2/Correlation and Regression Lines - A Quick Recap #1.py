import math

x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

xx = [i ** 2 for i in x]
yy = [i ** 2 for i in y]
xy = [x[i] * y[i] for i in range(len(x))]

r = (len(x) * sum(xy) - sum(x) * sum(y)) / math.sqrt((len(x) * sum(xx) - math.pow(sum(x), 2)) * (len(y) * sum(yy) - math.pow(sum(y), 2)))

print(round(r, 3))