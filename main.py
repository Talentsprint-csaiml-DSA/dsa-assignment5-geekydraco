def min_coins(coins, target_amount):
    # Initialize the DP array with infinity
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Fill the DP array
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[target_amount] is still infinity, return -1
    return dp[target_amount] if dp[target_amount] != float('inf') else -1