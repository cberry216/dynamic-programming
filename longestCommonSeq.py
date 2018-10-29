def getLCSSeq(path, seq):
    i = len(path) - 1
    j = len(path[0]) - 1

    subSeq = ""

    while i >= 1 and j >= 1:
        next = path[i][j]
        # If the next sequences is diagonal
        if (i - next[0]) == 1 and (j - next[1]) == 1:
            subSeq = seq[j - 1] + subSeq
        i = next[0]
        j = next[1]

    return subSeq


def longestCommonSeq(seq1, seq2):
    """Takes two string representation of sequences and returns the longest common sequence between the two sequences

    Arguments:
        seq1 {string} -- first sequences
        seq2 {string} -- second sequences
    """
    X = 'X' + seq1
    Y = 'X' + seq2

    LCS = [[0 for j in range(len(Y))] for i in range(len(X))]
    Path = [[0 for j in range(len(Y))] for i in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y)):
            if i == 0 or j == 0:
                LCS[i][j] = 0
                Path[i][j] = (0, 0)
            elif X[i] == Y[j]:
                LCS[i][j] = 1 + LCS[i - 1][j - 1]
                Path[i][j] = (i - 1, j - 1)
            else:
                maxLCS = max(LCS[i - 1][j], LCS[i][j - 1])
                if maxLCS == LCS[i][j - 1]:
                    Path[i][j] = (i, j - 1)
                if maxLCS == LCS[i - 1][j]:
                    Path[i][j] = (i - 1, j)
                LCS[i][j] = maxLCS

    return LCS[len(seq1)][len(seq2)], getLCSSeq(Path, seq2)


print(longestCommonSeq("ANSBSADBAIBDAS", "JBASDFKHBDASJFBA"))

p = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
     [(0, 0), (0, 1), (0, 2), (0, 3), (0, 3), (1, 4), (0, 5)],
     [(0, 0), (1, 0), (2, 1), (2, 2), (1, 4), (1, 4), (2, 5)],
     [(0, 0), (2, 1), (2, 2), (2, 2), (3, 3), (2, 5), (2, 6)],
     [(0, 0), (3, 0), (3, 2), (3, 3), (3, 4), (3, 4), (4, 5)],
     [(0, 0), (4, 1), (4, 1), (4, 3), (4, 4), (4, 5), (4, 6)],
     [(0, 0), (5, 1), (5, 2), (5, 3), (5, 3), (5, 5), (5, 5)],
     [(0, 0), (6, 0), (6, 2), (6, 3), (6, 4), (6, 4), (6, 6)]]
seq = "BDCABA"

# print(getLCSSeq(p, seq))
