ps = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3] 
hs = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

ph = [ps[i] * hs[i] for i in range(len(ps))]
pp = [i**2 for i in ps]

x = (sum(hs) * sum(pp) - sum(ps) * sum(ph)) / (len(ps) * sum(pp) - sum(ps) ** 2)
y = (len(ps) * sum(ph) - sum(ps) * sum(hs)) / (len(ps) * sum(pp) - sum(ps) ** 2)

r = x + y * 10

print(round(r,1))
