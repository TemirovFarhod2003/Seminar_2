def recsum(a, b):
    if b == 0:
        return a
    return 1 + recsum(a, b - 1)

print(recsum(2, 2))