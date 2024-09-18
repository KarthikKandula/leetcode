class Solution:
    """
    Use two pointer sliding window method to solve the problem
        doing this we get to compare each variable with each other

    Use two pointers - buy & sell assigned to 0th & 1st index respectively
        so we get to go thru the entire input in a sliding window method
    
    Loop thru input as long as sell < length of input
        calculate profit & replace maxProfit along the way
        check if sell price is less than buy price
            if yes, we have found a new low price to buy
        increment sell in each iteration to compare next price
    """
    def maxProfit(self, prices: List[int]) -> int:
        # Define buy & sell pointers (left & right) - buy at 0th index, sell at 1st index
        buy, sell = 0, 1
        maxP = 0 # variable to save max profit

        # loop while sell < length of input prices
        while sell < len(prices):
            # calculate temp profit for this iteration
            tempP = prices[sell] - prices[buy]
            maxP = max(maxP, tempP) # get max profit

            # check if sell price is less than buy price, if yes, found a new low buy price
            if prices[sell] < prices[buy]:
                buy = sell # assign sell to buy

            # increment sell to compare next price
            sell += 1

        # return maxProfit
        return maxP