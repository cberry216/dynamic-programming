"""
This solution can be optimized by using an array of size [2][sum + 1] instead of an array of size[n + 1][sum + 1]. Since each iteration on i only uses the row before it you don't need to keep track of every row before a given row, just the one before it.
"""


def subsetSumDP(set, sum):
    n = len(set)

    S = [[False for i in range(sum + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(sum + 1):
            if j == 0:
                S[i][j] = True
            elif i > 0:
                subIndex = j - set[i - 1]
                if subIndex >= 0:
                    S[i][j] = S[i - 1][j] or S[i][subIndex]
                else:
                    S[i][j] = S[i - 1][j]
            else:
                S[i][j] = False

    return S[n][sum]


S = [3, 34, 4, 12, 5, 2]
sum = 23

print(subsetSumDP(S, sum))
