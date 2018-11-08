from math import floor


def smallestBiggerThanBinSearch(array, L):
    x = 1
    length = len(array)
    i = 0
    # TODO: make function for this
    j = floor(length / (2 ** x))
    while i != j:
        i = j
        n = array[i]
        x += 1
        if n > L:
            j = i - floor(len / (2 ** x))
