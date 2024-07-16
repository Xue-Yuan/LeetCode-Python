from typing import List, FrozenSet
import math


def minCost(menu: List[List[str]], wishlist: set[str]) -> float:
    memo = {}

    def dfs(wishlist: FrozenSet[str]) -> float:
        if not wishlist:
            return 0

        if wishlist in memo:
            return memo[wishlist]

        minCost = math.inf
        for combo in menu:
            cost, items = combo
            items = set(items.split(","))
            if wishlist & items:
                minCost = min(dfs(wishlist - items) + float(cost), minCost)

        memo[wishlist] = minCost
        return minCost

    return dfs(frozenset(wishlist))


if __name__ == "__main__":
    menu = [['5.00', "pizza"], ['8.00', "sandwich,coke"], ['4.00', "pasta"],
            ['2.00', "coke"], ['6.00', "pasta,coke,pizza"],
            ['8.00', "burger,coke,pizza"], ['5.00', "sandwich"]]

    wishlist = set(["burger", "pasta"])

    print(minCost(menu, wishlist))
