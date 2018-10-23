def catalanNumber(n):
    # Base Case
    if n == 0:
        return 1
    sum = 0
    for i in range(0, n):
        sum += catalanNumber(i) * catalanNumber(n - 1 - i)
    return sum


print(catalanNumber(9))


def catalanNumberDP(n):
    if n <= 1:
        return 1

    # Initialize cache
    cache = [0] * (n + 1)
    cache[0] = 1
    cache[1] = 1

    for i in range(1, n + 1):
        sum = 0
        for j in range(0, i):
            sum += cache[j] * cache[i - 1 - j]
        cache[i] = sum

    return cache[n]


print(catalanNumberDP(9))
