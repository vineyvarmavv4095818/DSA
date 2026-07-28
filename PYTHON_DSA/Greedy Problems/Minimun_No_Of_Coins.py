def solve(N, coins):
    result = []
    n = len(coins)

    for i in range(n-1, -1, -1):
        while N >= coins[i]:
            result.append(coins[i])
            N -= coins[i]
    return result

n = 41
coins = [1,2,5,10,20,50,100,200,500,2000]
print(solve(n, coins))

# TC = O(N)
# SC = O(1)