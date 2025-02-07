class Solution:
    """
    this is a simple clean strategy
        that just relies on the changes in price on a daily basis
        since we can do infinite amount of transactions but can only hold one stock at a time
        we only need to compare with the previous day's value & settle those immediately
        once we add all the consecutive difference values, we get the final value
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # variable to hold profit

        # loop from 1st index, skipping location 0
        for i in range(1, len(prices)):
            # if current price is higher than previous price
            if prices[i] > prices[i - 1]:
                # add the difference to profit variable
                profit += (prices[i] - prices[i - 1])

        # return profit value
        return profit

    """
    use dp techniques to calculate the differences between each day's values
        we can do two possible operations
            skip that day -- we can choose not to buy or sell this day, possibility of higher price next day
            buy/sell -- do opposite of whatever operation was performed before
        by implementing these two operations, we get the max profit possible 
        by using a flag to indicate if bought/sold, we can accomodate multiple transactions for the input
    """
    def maxProfit(self, prices: List[int]) -> int:
        # cache to speed up dp
        cache = {}

        # recursive function to implement dp
        def dfs(i, buyFlag):
            # base conditions
            # if i reaches end of input
            if i == len(prices):
                return 0
            
            # if this index & flag is already in the cache, return that value
            if (i, buyFlag) in cache:
                return cache[(i, buyFlag)]

            # skip to next
            skip = dfs(i + 1, buyFlag)

            ops = 0 # variable to hold return val

            # if bought/sold
            # if buyFlag is True
            if buyFlag:
                ops = dfs(i + 1, False) # call for next index making flag false, indicating sold
                ops += prices[i] # add current index price to ops

            # if not bought, buy
            else:
                ops = dfs(i + 1, True) # call for next index making flag True, indicating brought
                ops -= prices[i] # subtract current index price to ops

            # save max value of skip or bought/sold to cache
            cache[(i, buyFlag)] = max(skip, ops)

            # return value from cache
            return cache[(i, buyFlag)]
            # return max(skip, ops)

        # initial func call to dfs func
        return dfs(0, False)
