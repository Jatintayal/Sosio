from math import degrees, atan2

AB = int(input())
BC = int(input())

ACB = degrees(atan2(AB, BC))

MBC = ACB

print(str(round(MBC)) + '°')
