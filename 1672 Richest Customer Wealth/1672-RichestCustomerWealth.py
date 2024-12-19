class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # variable to track max wealth
        maxVal = 0

        # loop thru input accounts
        for i in range(len(accounts)):
            # calculate the sum of current customer
            tempSum = sum(accounts[i])

            # get max of current max wealth or current customer wealth
            maxVal = max(maxVal, tempSum)
        
        # return max wealth
        return maxVal
