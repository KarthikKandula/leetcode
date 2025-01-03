class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # get sum of all elements in input
        total = sum(nums)
        leftSum = 0 # variable to calc running left sum

        res = 0 # create result variable -- holds num of valid splits

        # loop for each value in input -- other than last since at least one element should be to the right of i
        for i in range(len(nums) - 1):
            total -= nums[i] # subtract current value from total
            leftSum += nums[i] # add current value to leftSum

            # if leftSum is greater than total i.e right sum
            if leftSum >= total:
                res += 1 # append result value
        
        # return result
        return res
