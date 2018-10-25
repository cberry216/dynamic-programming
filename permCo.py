# P(n, k) = P(n-1, k) + k* P(n-1, k-1)


def permCoDP(n, k):
    if k == 0 or k == n:
        return 1

    C = [0 for i in range(n + 1)]
    C[0] = 1
    C[1] = 1

    for i in range(2, n + 1):
        C[i] = i * C[i - 1]

    return int(C[n] / C[n - k])


print(permCoDP(6, 3))
