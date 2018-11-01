def getItems(P):
    i = len(P) - 1
    w = len(P[0]) - 1

    items = []

    while i >= 1 and w >= 1:
        next = P[i][w]
        if next[1] < w:
            items.append(i)
        i = next[0]
        w = next[1]

    return items


def knapsackDP(items, weight):

    WEIGHT = 0
    BENEFIT = 1

    n = len(items)

    B = [[0 for w in range(weight + 1)] for i in range(n + 1)]
    P = [[0 for w in range(weight + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(weight + 1):
            if i == 0 or w == 0:
                B[i][w] = 0
                P[i][w] = (0, 0)
            else:
                if items[i - 1][WEIGHT] > w:
                    B[i][w] = B[i - 1][w]
                    P[i][w] = (i - 1, w)
                else:
                    val = max(B[i - 1][w], B[i - 1][w - items[i - 1]
                                                    [WEIGHT]] + items[i - 1][BENEFIT])
                    B[i][w] = val
                    if val == B[i - 1][w]:
                        P[i][w] = (i - 1, w)
                    else:
                        P[i][w] = (i - 1, w - items[i - 1][WEIGHT])
    return B[n][weight], getItems(P)


a = [(1, 15), (5, 10), (4, 9), (3, 5)]
print(knapsackDP(a, 8))
