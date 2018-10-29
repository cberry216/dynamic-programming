def editDistanceDP(A, B):
    D = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]

    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if i == 0:
                D[i][j] = j
            elif j == 0:
                D[i][j] = i
            elif A[i - 1] == B[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])

    return D[len(A)][len(B)]


print(editDistanceDP("kitten", "sitting"))
