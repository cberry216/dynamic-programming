# Divides a by b as many times as possible
def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a


def isUgly(n):
    n = maxDivide(n, 2)
    n = maxDivide(n, 3)
    n = maxDivide(n, 5)
    return True if n == 1 else False


def uglyNumber(n):
    currentNumber = 1
    count = 1  # number of ugly numbers

    while n > count:
        currentNumber += 1
        if isUgly(currentNumber):
            count += 1
    return currentNumber


print(uglyNumber(150))

# DP Method

# We want to create three sequences for multiples of 2, 3, and 5
#   a2 = [1*2, 2*2, 3*2, 4*2, ... , n*2]
#   a3 = [1*3, 2*3, 3*3, 4*3, ... , n*3]
#   a5 = [1*5, 2*5, 3*5, 4*5, ... , n*5]


def nextMultipleofN(i, array, n):
    if n != 2 or n != 3 or n != 5:
        raise ValueError("Divisor must be 2, 3, or 5.")
    return array[i] * n


def uglyNumberDP(n):
    # Initialized array
    ugly = [0] * (n)
    ugly[0] = 1

    # Pointers to point to first element of ugly array
    i2 = 0
    i3 = 0
    i5 = 0

    # Initialize next ugly number choices
    nextMultipleOf2 = ugly[0] * 2
    nextMultipleOf3 = ugly[0] * 3
    nextMultipleOf5 = ugly[0] * 5

    for i in range(1, n):
        nextUglyNo = min(nextMultipleOf2,
                         nextMultipleOf3,
                         nextMultipleOf5)

        ugly[i] = nextUglyNo

        if nextUglyNo == nextMultipleOf2:
            i2 += 1
            nextMultipleOf2 = ugly[i2] * 2
        if nextUglyNo == nextMultipleOf3:
            i3 += 1
            nextMultipleOf3 = ugly[i3] * 3
        if nextUglyNo == nextMultipleOf5:
            i5 += 1
            nextMultipleOf5 = ugly[i5] * 5

    return ugly[n - 1]


print(uglyNumberDP(150))
