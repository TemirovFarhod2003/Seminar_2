def reverseNum(n, rem=0):
    if n == 0:
        return (rem) // 10
    else:
        return reverseNum(n // 10, (rem + (n % 10)) * 10)


print(reverseNum(123))
