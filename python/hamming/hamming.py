def distance(a, b):
    d = 0
    a, b = list(a), list(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            d += 1
    return d
