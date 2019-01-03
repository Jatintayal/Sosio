import math

bxy = 5/4
byx = 20/9

r = math.sqrt(bxy * byx)

dev_y = byx * 3 / r
var_y = dev_y ** 2

print(var_y)