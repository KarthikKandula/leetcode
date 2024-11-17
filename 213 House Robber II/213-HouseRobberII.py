class Solution:
    """
    this approach implements a constant space to this dp problem
        we're reusing House Robber 1 solution but with a twist
        we're treating this as two different problems where
            the input is including 0th index but eliminating last value
            the input is eliminating 0th index but including last value
        essentially we need to check two different solutions
            max value including 0th index but eliminating last value
            max value eliminating 0th index but including last value
    """
    def rob(self, nums: List[int]) -> int:

        # return the max of 
        # first element -- in case input only has 1 element
        # array eliminating 0th index but including last value
        # array including 0th index but eliminating last value
        return max(nums[0], self.basicHouseRobber(nums[1:]), self.basicHouseRobber(nums[:-1]))

    # helper function -- implementing basic house robber solution
    def basicHouseRobber(self, nums:List[int]) -> int:
        # create two variables to record max values for prev 2 values
        rob1, rob2 = 0, 0

        # loop for each number
        for n in nums:
            # get max of current num + max of 2 nums before or max of prev num
            tempRob = max(rob1 + n, rob2)
            rob1 = rob2 # assign rob2 to rob1 -- setting values up for next iteration
            rob2 = tempRob # assign temp value to rob2 -- setting the current max value to rob2, again setting up for next iteration

        # return rob2 since that value has the max value as of the last value in input
        return rob2


    """
    Recursion w/ Memoization
    """
    # def rob(self, nums: List[int]) -> int:

    #     # create cache array to store values
    #     # this is a 2D array since there might be different values for True & False flows
    #     cache = [[-1] * 2 for _ in range(len(nums))]

    #     # create recursive function
    #     def dfs(i, flag):
    #         # if input is overshot, return 0 -- default value
    #         if i >= len(nums):
    #             return 0

    #         # if flag is true & index is the last index -- skip this since houses are circular
    #         if flag == True and i == len(nums) - 1:
    #             return 0

    #         # check if current index & flag in memo has any value
    #         if cache[i][flag] != -1:
    #             return cache[i][flag] # if it does, return that value -- avoiding additional function calls

    #         # if cache doesn't have values, perform function calls & append result to cache
    #         # call for next function, add current value while calling for the 2nd next num
    #         cache[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))

    #         # return value from cache
    #         return cache[i][flag]
        
    #     # return the max of 
    #     # first element -- in case input only has 1 element
    #     # function call for 0th index & flag true to indicate not to count last element
    #     # function call for 1st index & flag false to indicate to count last element
    #     return max(nums[0], dfs(0, True), dfs(1, False))
    
    """
    Recursion w/o Memoization
    """
    # def rob(self, nums: List[int]) -> int:
        
    #     # create recursive function
    #     def dfs(i, flag):
    #         # if input is overshot, return 0 -- default value
    #         if i >= len(nums):
    #             return 0

    #         # if flag is true & index is the last index -- skip this since houses are circular
    #         if flag == True and i == len(nums) - 1:
    #             return 0 # return 0
            
    #         # call for next function, add current value while calling for the 2nd next num
    #         return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
        
    #     # return the max of 
    #     # first element -- in case input only has 1 element
    #     # function call for 0th index & flag true to indicate not to count last element
    #     # function call for 1st index & flag false to indicate to count last element
    #     return max(nums[0], dfs(0, True), dfs(1, False))