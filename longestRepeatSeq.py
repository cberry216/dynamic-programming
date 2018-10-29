def getLRS(P, str):
    i = len(P) - 1
    j = len(P) - 1

    subSeq = ""

    while i >= 1 and j >= 1:
        next = P[i][j]
        if (i - next[0]) == 1 and (j - next[1]) == 1:
            subSeq = str[i - 1] + subSeq
        i = next[0]
        j = next[1]

    return subSeq


def longestRepeatSeqDP(str):

    A = 'X' + str
    n = len(str)

    S = [[0 for j in range(n + 1)] for i in range(n + 1)]
    P = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i] == A[j] and i != j:
                S[i][j] = 1 + S[i - 1][j - 1]
                P[i][j] = (i - 1, j - 1)
            else:
                val = max(S[i - 1][j], S[i][j - 1])
                S[i][j] = val
                if val == S[i - 1][j]:
                    P[i][j] = (i - 1, j)
                else:
                    P[i][j] = (i, j - 1)

    return S[n][n], getLRS(P, str)


print(longestRepeatSeqDP("ATACTCGGA"))
