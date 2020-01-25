def base_change(n, b):
    a = list()

    while n > 0:
        a.append(n % b)
        n //= b

    for i in range(0, int(len(a)//2)):
        a[i], a[n-1-i] = a[n-1-i], a[i]

    return a


print(base_change(111, 7))

