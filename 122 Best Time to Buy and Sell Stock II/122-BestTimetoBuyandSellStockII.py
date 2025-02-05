class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dfs(i, buyFlag, profit):
            # base conditions
            if i == len(prices):
                return profit
            
            if (i, buyFlag) in cache:
                return cache[(i, buyFlag)]

            # skip to next
            skip = dfs(i + 1, buyFlag, profit)

            ops = 0

            # if bought, sell
            if buyFlag:
                profit += prices[i]
                ops = dfs(i + 1, False, profit)

            # if not bought, buy
            else:
                profit -= prices[i]
                ops = dfs(i + 1, True, profit)

            # print(f'i {i}, skip {skip}, ops {ops}, max {max(skip, ops)}')

            cache[(i, buyFlag)] = max(skip, ops)

            return cache[(i, buyFlag)]
            # return max(skip, ops)

        return dfs(0, False, 0)
