#STEP1
## Recursion
# TC = O(2^N)
# SC = O(N)

def fib(num):
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)

print(fib(4))

#STEP2
## recursion + memoization (top-down)
# TC = O(N)
# SC = O(N) + O(N)    (stack space + dp arrray)

def fib(num):
    if num <= 1:
        return num
    if dp[num] != -1:
        return dp[num]

    dp[num] = fib(num-1) + fib(num-2)
    return dp[num]

num = 5
dp = [-1] * (num+1)
print(fib(4))

#STEP3
## tabulation method (Bottum-up)
# TC = O(N)
# SC = O(N)   (dp array)

def fib(n):
    for num in range(2, n+1):
        dp[num] = dp[num-1] + dp[num-2]

    return dp[n]

n = 5
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1

print(fib(4))

#STEP4
## Space Optimized
# TC = O(N)
# SC = O(1)

def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 1
    prev2 = 0
    for i in range(2, n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev

n = 5
print(fib(4))