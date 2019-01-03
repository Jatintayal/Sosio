from collections import Counter
c = Counter(sorted(input()))
for i in c.most_common(3): 
    print(*i)