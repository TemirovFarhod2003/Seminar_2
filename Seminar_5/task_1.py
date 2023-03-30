def func(num, even = 0, odd = 0):
    if not num:
        return even, odd
    if num % 10 % 2 == 1:
        odd += 1
    else:
        even += 1
    return func(num // 10, even, odd)


n = int(input())
print(func(n))
