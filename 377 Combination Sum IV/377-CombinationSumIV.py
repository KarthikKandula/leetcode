class Solution:
    """
    this is a bottom up solution focusing on finding permutations
        instead of finding the no. of ways from the top, we find the no. of ways from bottom to top
        we try to find how many ways there are to find every sum between 1 -> target
        using the previous computed sums, we find next numbers

    create a cache to track the no. of times a sum can be formed
        initialize 0 --> 1 since there is exactly 1 way to form the sum 0, but using no elements
        now loop for each possible total value until target
        loop thru each number in input 
            add the no. of times this total can be formed by adding the number from nums i.e total - n
            add the no. of times to this total to the cache
        do this until target & we have the no. of combinations in the cache
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # create cache for the problem
        dp = {0: 1}

        # loop for each total value form 1 -> target
        for total in range(1, target + 1):
            # initialize this total value to 0, initially zero ways to form this sum
            dp[total] = 0

            # now, loop for each numbers in nums
            for n in nums:
                # add any possible way where we can get to this total by subtracting current n
                dp[total] += dp.get(total - n, 0)
        
        # return value for target from cache
        return dp[target]
