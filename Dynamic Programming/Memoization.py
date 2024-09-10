def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)  # Corrected the recursive call

memo = [None] * 100

def fibMemo(n):
    if memo[n] is not None:  # Check if already calculated
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fibMemo(n - 1) + fibMemo(n - 2)  # Use fibMemo for memoization
    return memo[n]

n = 7
#print(fib(n))
print(fibMemo(n))
