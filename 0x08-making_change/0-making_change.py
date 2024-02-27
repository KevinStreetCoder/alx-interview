#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    Args:
        coins (list): A list of the values of the coins in possession
        total (int): The total amount to be achieved
    Returns:
        int: Fewest number of coins needed to meet total
    """
    if total < 1:
        return 0

    # Initialize a list to store the minimum number of coins required for each total amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update min_coins list for each total amount
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1

