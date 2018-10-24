def binCo(n, k):
    if k == 0 or k == n:
        return 1
    return binCo(n - 1, k - 1) + binCo(n - 1, k)


print(binCo(10, 2))


def binCoDP(n, k):
    if k == 0:
        return 1

    C = [[0 for i in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


print(binCoDP(10, 2))
