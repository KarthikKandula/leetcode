class Solution:
    """
    this approach implements a constant space to this dp problem
        what it's doing is effectively calculating the max possible value at each location
        saving these values to two values & keep moving along the array in one pass

    take two values initialized to 0

    loop for input nums
        calc the max of prev 1st index + current value & the prev value
            adding n to only the 1st value skipping immediate adjacent value
        assign rob2 to rob1 -- shifting values
        assign temp to rob2 -- shifting values done
    
    return rob2 at the end since the last value has max value
    """
    def rob(self, nums: List[int]) -> int:
        # create two variables to record max values for prev 2 values 
        rob1, rob2 = 0, 0

        # loop for each number
        for n in nums:
            # get max of current num + max of 2 nums before or max of prev num
            temp = max(n + rob1, rob2)
            rob1 = rob2 # assign rob2 to rob1 -- setting values up for next iteration
            rob2 = temp # assign temp value to rob2 -- setting the current max value to rob2, again setting up for next iteration

        # return rob2 since that value has the max value as of the last value in input
        return rob2

    """
    Better memoization approach
        this approach is only making calls for the next two indexes
        it's only adding the current value to the 2nd index
            so it's effectively skipping adding current value to next 1st index

    this implements the same regular recursive approach but elimates a layer of recursive function calls

    take an array initialized to -1 for the length of input n
        -1 indicates this value isn't yet calculated
    
    now in a function call before making recursive calls
        check if the array has been initialized at this index
        if it is, return the value -- reducing the amount of function calls by reusing them effectively

    before returning, get the max value of the
        return value of next 1st index
        current value + return value of next 2nd index
    """
    # def rob(self, nums: List[int]) -> int:
        
    #     # create cache array to store values
    #     memo = [-1] * len(nums)

    #     # create recursive function
    #     def dfs(i):
    #         # if input is overshot, return 0 -- default value
    #         if i >= len(nums):
    #             return 0
            
    #         # check if current index in memo has any value
    #         if memo[i] != -1:
    #             return memo[i] # if it does, return that value -- avoiding additional function calls
            
    #         # if cache doesn't have values, perform function calls & append result to cache
    #         # call for next function, add current value while calling for the 2nd next num
    #         memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))

    #         # return value from cache
    #         return memo[i]
        
    #     return dfs(0)

    """
    My solution - 2^N run time

    2^N run time is happening since we're calling all the possible values skipping the next value
        since there are multiple calls happening for each index, it's 2^N
    """
    # def rob(self, nums: List[int]) -> int:
        
    #     # create cache array to store values
    #     cache = [-1] * len(nums)

    #     # create recursive function
    #     def dfs(i):
    #         # if input is overshot, return 0 -- default value
    #         if i >= len(nums):
    #             return 0

    #         # check if current index in memo has any value
    #         if cache[i] != -1:
    #             return cache[i] # if it does, return that value -- avoiding additional function calls
            
    #         # create a result variable
    #         res = 0

    #         # loop for each index in input from range i + 2 to end -- skipping next num
    #         for eachIndex in range(i + 2, len(nums)):
    #             temp = dfs(eachIndex) # get temp return value
    #             res = max(temp, res) # get the max value
            
    #         # add the max value to current location value & store it in cache
    #         cache[i] = res + nums[i]

    #         # return cache value
    #         return cache[i]
        
    #     # return the max of 1st & 2nd index calls
    #     return max(dfs(0), dfs(1))
