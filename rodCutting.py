def rodCutDP(cost):
    P = [0 for i in range(len(cost) + 1)]

    P[0] = 0

    for i in range(1, len(cost) + 1):
        maxVal = 0
        for j in range(i):
            maxVal = max(maxVal, P[j] + cost[i - j - 1])
        P[i] = maxVal

    return P[len(cost)]


print(rodCutDP([1, 5, 8, 9, 10, 17, 17, 20]))
