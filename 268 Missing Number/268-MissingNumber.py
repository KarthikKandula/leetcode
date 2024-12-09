class Solution:
    """
    the idea is to use a mathematical trick to solve the problem
        In a complete array with no missing number, The sum of the indices matches the sum of the values
        The sum of indices and the sum of values in nums cancel out for all numbers except the missing one.
        The algorithm avoids explicitly calculating the sums of indices and values. Instead, it adjusts res dynamically during iteration.
    """
    def missingNumber(self, nums: List[int]) -> int:
        # initialize result variable with length of input nums
        res = len(nums)

        # loop for length of input nums
        for i in range(len(nums)):
            # add the difference of index - value to result
            res += (i - nums[i])

        # return result
        return res
