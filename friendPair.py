def friendPairDP(n):
    P = [0 for i in range(n + 1)]
    P[0] = 1
    P[1] = 1

    for i in range(2, n + 1):
        # P[i] = (i - 1) + 2 * (P[i - 1] - 1)
        P[i] = P[i - 1] + (i - 1) * P[i - 2]

    return P[n]


print(friendPairDP(6005))
