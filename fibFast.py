# We will be solving the Fibonacci sequence
# Begin by creating the basic recursive function

# FIRST, find the FIRST solution


def fib0(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib0(n-1) + fib0(n-2)


print(fib0(5))

# ANALYZE the solution

# This is an inefficient way to solve the Fibonacci sequence
# It wil run in Θ(2^n)
#   1 -> 2 -> 4 -> ... -> 2^n

# To solve a problem using DP, it must have:
#   1: Optimal Substructure (an optimal solution can be constructed efficiently from optimal solutions of its subproblems)
#       |> We can get the right answer by combining our solutions to the subproblems
#   2: Overlapping Subproblems (if the problem can be broken down into subproblems which are reused several times)
#       |> Calling fib(5) results in fib(4) and fib(3), calling fib(4) calls fib(3) and fib(2), fib(5) and fib(4) both call fib(3).


# SUBPROBLEMS, identify the SUBPROBLEMS

# In this case the subproblems are just the recursive calls to fib.
# Now that we know the subproblems, we can memoize the solutions.

def fib1(n):
    # Base case for  Fibonacci
    if n < 2:
        return n
    # Initialize array of length n+1
    cache = [-1] * (n + 1)
    # Initialize base case values
    cache[0] = 0
    cache[1] = 1

    return fib2(n, cache)


def fib2(n, cache):
    # If the value is already stored in the cache
    if cache[n] >= 0:
        return cache[n]
    # Else, compute the result and store it in the cache
    print(cache)
    cache[n] = fib2(n - 1, cache) + fib2(n - 2, cache)
    # Return cache
    return cache[n]


print(fib1(5))


# TURN around the solution

# Basically we are turning our solution from a recursive function to an iterative function

def fibN(n):
    if n == 0:
        return 0

    # Initialize cache
    cache = [0] * (n + 1)
    cache[1] = 1

    # Fill cache iteratively
    for i in range(2, n + 1):
        cache[i] = cache[i-1] + cache[i - 2]
    return cache[n]


print(fibN(5))
