import sys

"""
    1st approach: dynamic programming
    - on each day, we might either have a stock or dont have any stock
    - calculate our gain in both cases
    - gain on each day is a sub-problem

    Time    O(n)
    Space   O(1)
    652 ms, faster than 32.85%
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -sys.maxsize
        for price in prices:
            # actually we dont need this temp variable
            # temp = hold
            # because if we sell and buy a stock on the same day, your total gain must be less than just hold
            # due to the transaction fee

            # remain the cash OR to sell our asset
            # sell out asset = cash out the hold + cur price = all the cash we have
            cash = max(cash, hold+price)
            # remain the hold OR to buy in a stock
            # buy in stock = we need to buy in the current stock, therefore need to subtract the fee
            hold = max(hold, cash-price-fee)
        # return cash, hold
        return cash


a = [1, 3, 2, 8, 4, 9]
b = 2
print(Solution().maxProfit(a, b))

a = [1, 3, 7, 5, 10, 3]
b = 3
print(Solution().maxProfit(a, b))

print("-----")

"""
    2nd approach: dynamic programming
    - on each day, we might either have a stock or dont have any stock
    - calculate our gain in both cases
    - gain on each day is a sub-problem

    Time    O(n)
    Space   O(1)
    652 ms, faster than 32.85%
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        # at the very begining, we dont have money, but we still purchase therefore we have negative asset
        hold = -prices[0]-fee
        for i in range(1, len(prices)):
            price = prices[i]
            # remain the cash OR to sell our asset
            # sell out asset = cash out the hold + cur price = all the cash we have
            cash = max(cash, hold+price)
            # remain the hold OR to buy in a stock
            # buy in stock = we need to buy in the current stock, therefore need to subtract the fee
            hold = max(hold, cash-price-fee)
        # return cash, hold
        return cash


a = [1, 3, 2, 8, 4, 9]
b = 2
print(Solution().maxProfit(a, b))

a = [1, 3, 7, 5, 10, 3]
b = 3
print(Solution().maxProfit(a, b))