## Recursion

def solve(index):
    if index == 0:
        return nums[index]
    if index < 0:
        return 0

    pick = nums[index] + solve(index-2)
    not_pick = solve(index-1)
    return max(pick, not_pick)

nums = [2,7,9,3,1]
print(solve(4))