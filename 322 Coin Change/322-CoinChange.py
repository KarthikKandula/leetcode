class Solution:
    """
    we can treat this as a dfs problem
        we need to calculate the no. of coins needed for the amount
        we can put a slight twist into the problem
            instead of calculating for each coin & starting from 0
            we can start in desc order from the input amount
            for each coin, subtract the coin's value from needed amount & call recursive function for new wanted value
            get the min value out of all the coins 
    
    create a helper function to implement dfs recursively
        base conditions
            if amount == 0, return 0
        create a variable with max value 
        loop thru all the coins
            check if using the coin won't put value into negative
            if it doesn't, recursively call for the remainder for this coin
                add 1 to indicate this coin has been used
                get the min value of return & above result variable
            after all coins are done, we have the min value in result varaible
        return this value
    
    the return value of initial call for amount will have the no. of coins
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # create output variable w/ max value -- here it's amount + 1
        out = amount + 1

        # create cache to reduce func calls
        cache = [-1] * (amount + 1)
        cache[0] = 0 # initialize 0 amount to 0

        def dfs(amt):
            # base conditions
            # if amount is 0, no coins needed for 0 amt
            if amt == 0:
                return 0
            # if this value already exists in cache, return it, reducing func calls
            if cache[amt] != -1:
                return cache[amt]
            
            # initialize result to max value
            res = amount + 1

            # loop thru each coin
            for coin in coins:
                # if using this coin is not -ve
                if amt - coin >= 0:
                    # update result
                    res = min(res, 1 + dfs(amt - coin))
                    # get the min value of current res
                    # recursively call the difference needed for this coin for this amount -- adding 1 since using this coin

            # save value in cache before returning
            cache[amt] = res

            # return value from cache
            return cache[amt]
        
        # initial function call for amount
        out = dfs(amount)
        
        # return output if value has changed, else return -1
        return out if out != amount + 1 else -1

