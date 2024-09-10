n = 6  # The position in the Fibonacci sequence we want to calculate

# Create a list to store Fibonacci numbers up to n
dp = [None] * (n + 1)

print(dp)

# Base cases
dp[0] = 0  # F(0) = 0
dp[1] = 1  # F(1) = 1

# Calculate Fibonacci numbers from 2 to n
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]  # F(i) = F(i-1) + F(i-2)

print(n)
print(dp[i])
print(dp[i - 1])
print(dp[i - 2])


# Print the nth Fibonacci number
print(dp[n])  # Output: 8



def fib(n):
    dp = [None] * (n + 1)  # Line 2
    dp[0] = 0              # Line 3
    dp[1] = 1              # Line 4
    for i in range(2, n + 1):  # Line 5
        dp[i] = dp[i - 1] + dp[i - 2]  # Line 6
    return dp[n]            # Line 7

n = 6                       # Line 8
print(fib(n))               # Line 9