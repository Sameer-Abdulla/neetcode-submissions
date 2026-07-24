class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        m_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit<0:
                l = r
            m_profit = max(m_profit, profit)
            r+=1
        return m_profit

        