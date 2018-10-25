def goldMine(mat):
    C = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]

    for col in range(len(mat) - 1, -1, -1):
        for row in range(len(mat[col])):
            if col == len(mat) - 1:
                C[col][row] = mat[col][row]
            else:
                if row == 0:
                    rightUp = 0
                else:
                    rightUp = C[col + 1][row - 1]

                if row == len(mat[row]) - 1:
                    rightDown = 0
                else:
                    rightDown = C[col + 1][row + 1]

                right = C[col + 1][row]

                C[col][row] = mat[col][row] + max(rightDown, right, rightUp)

    return max(C[0])


a = [[1, 2, 1], [3, 1, 4], [6, 4, 1]]
print(goldMine(a))

b = [[1, 2, 0], [3, 1, 6], [3, 4, 4]]
print(goldMine(b))

c = [[10, 22, 5, 0], [33, 21, 0, 6], [13, 4, 2, 14], [15, 1, 3, 2]]
print(goldMine(c))
