def assemblyLineDP(a, t, e, x):

    n = len(a[0])

    T1 = [0 for i in range(n + 1)]
    T2 = [0 for i in range(n + 1)]

    T1[1] = e[0] + a[0][0]
    T2[1] = e[1] + a[1][0]

    for i in range(2, n + 1):
        T1[i] = min(T1[i - 1] + a[0][i - 1], T2[i - 1] +
                    a[0][i - 1] + t[1][i - 1])  # a[0][i -1] is off by one so in reality it is a[0][i]
        T2[i] = min(T2[i - 1] + a[1][i - 1], T1[i - 1] +
                    a[1][i - 1] + t[0][i - 1])

    return min(T1[n] + x[0], T2[n] + x[1])


a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
print(assemblyLineDP(a, t, e, x))
