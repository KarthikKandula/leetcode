class Solution:
    """
    Better solution -- via neetcode

    the basic jist of this solution is to break the larger problem into sub problems
        when we have input [1, 2, 3]
            we're breaking up the above input to [2, 3]
                in turn breaking this to [3]
            while returning we're going to add the removed value in every index
                this will make the return value [2, 3] and [3, 2]
        at this point, we'll do the same -- add removed value at each index
            this will make the return value [1, 2, 3] etc., which will have all the results
    
    make recursive calls by removing first index from nums
        check if length of input is 0 -- base condition
        after adding value at each index return the result set
    
    return value of first call -- we get our result
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # check if length of nums is 0 -- recursive base condition
        if len(nums) == 0:
            return [[]] # return result set
        
        # make recursive call -- omitting first index
        perms = self.permute(nums[1:])
        res = [] # variable to store results

        # loop for each permutation from recursive call response
        for eachPerm in perms:
            # loop for each index in each permutation -- to add 0th index value at each location
            for index in range(len(eachPerm) + 1):
                eachPermCopy = eachPerm.copy() # make a copy of current permutation -- for future ops
                eachPermCopy.insert(index, nums[0]) # insert 0th value from nums at current index in permutation
                res.append(eachPermCopy) # append current copy to result set

        # return result set
        return res

    """
    Iterative approach
    """
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     # check if length of length of input nums is 1 -- return nums in it's own set 
    #     if len(nums) == 1:
    #         return [nums[:]]
        
    #     # result array
    #     res = []

    #     # loop for each element of nums
    #     for i in range(len(nums)):
    #         n = nums.pop(0) # pop first value in nums

    #         # recusively call for new nums -- without first value
    #         perms = self.permute(nums)

    #         # loop for each value in perms from recursive call response
    #         for eachPerm in perms:
    #             eachPerm.append(n) # append first popped value to each permutation
            
    #         # add all values from perms to result set
    #         res.extend(perms)

    #         # add popped value to end of nums -- rotating nums array so it'll pickup next value next time
    #         nums.append(n)
        
    #     # return result set
    #     return res


    """
    Alternate solution like regular backtracking

    learn later -- experiment with set
    """
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     res = []

    #     def dfs(perm):
    #         if len(perm) == len(nums):
    #             res.append(perm[:])
    #             return
            
    #         for i in range(len(nums)):
    #             if nums[i] in perm:
    #                 continue
    #             perm.append(nums[i])
    #             dfs(perm)
    #             perm.pop()
        
    #     dfs([])
    #     return res