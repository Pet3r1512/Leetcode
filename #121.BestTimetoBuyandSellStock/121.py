from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

solution_instance = Solution()

print(solution_instance.maxProfit([7,1,5,3,6,4]))
print(solution_instance.maxProfit([7,6,4,3,1]))