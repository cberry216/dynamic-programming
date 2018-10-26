def coinChangeDP(coins, value):
    C = [[0 for i in range(value + 1)] for i in range(len(coins) + 1)]

    for m in range(len(coins) + 1):
        for n in range(value + 1):
            if n == 0:
                C[m][n] = 1
            elif m > 0:
                subValue = n - coins[m - 1]
                if subValue < 0:
                    C[m][n] = C[m - 1][n] + 0
                else:
                    C[m][n] = C[m - 1][n] + C[m][subValue]
            else:
                C[m][n] = 0
    return C[len(coins)][value]


coins = [2, 5, 3, 6]
value = 115

print(coinChangeDP(coins, value))
