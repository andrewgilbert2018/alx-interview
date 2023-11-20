#!/usr/bin/python3
"""
Solution fot the coin change challenge
"""


def makeChange(coins, total):
    """"
    Logic to return the number of coins needed
    Args:
        coins: coins denomination
        total: expected value

    Returns:
        Number of coins needed or -1 if is not possible
    """
    if total <= 0:
        return(0)

    current = counter = 0
    while coins and total != current:
        max_coin = max(coins)
        if max_coin + current <= total:
            counter += 1
            current += max_coin
        elif max_coin + total > total:
            coins.remove(max_coin)
    return(counter if coins else -1)
