"""
Subset Sum Problem – Brute Force Example
"""

def subset_sum(nums, target):
    n = len(nums)
    solutions = []
    # try all 2^n subsets
    for mask in range(1 << n):
        current = []
        total = 0
        for i in range(n):
            if mask & (1 << i):
                current.append(nums[i])
                total += nums[i]
        if total == target:
            solutions.append(current)
    return solutions

if __name__ == "__main__":
    nums   = [3, 34, 4, 12, 5, 2]
    target = 9
    sols = subset_sum(nums, target)
    print(f"Subsets that sum to {target}:", sols)
