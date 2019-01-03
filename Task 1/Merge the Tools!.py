def merge_the_tools(string, k):
    n = len(string)
    t = []
    x = int(n/k)
    string = list(string)
    for i in range(x):
        t.append(without_repetition(string[k * i : k * (i + 1)]))
    [print(i) for i in t]

def without_repetition(t):
    s = set()
    o = []
    for c in t:
        if c not in s:
            s.add(c)
            o.append(c)
    return ''.join(o)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)