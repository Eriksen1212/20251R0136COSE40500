"""
0/1 Knapsack Problem – Dynamic Programming Example
"""

def knapsack(values, weights, capacity):
    n = len(values)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w], 
                    dp[i-1][w-weights[i-1]] + values[i-1]
                )
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

if __name__ == "__main__":
    values  = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_val = knapsack(values, weights, capacity)
    print(f"Maximum value in Knapsack = {max_val}")
