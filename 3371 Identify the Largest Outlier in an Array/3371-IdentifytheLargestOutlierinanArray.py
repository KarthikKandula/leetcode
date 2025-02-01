class Solution:
    """
    we can solve this problem using prefix sum
        the solution involves getting the sum of all values in nums
        we need to find the outlier
            the outlier can be found by 
                deducting any num from total -- diff
                if half value of this diff is in the array, it's a potential outlier
                but a condition exists, that the outlier should be different than current num
        
        so with this knowledge in mind we implement the below logic
            get prefix sum
            populate in a hashmap all values with their indexes
            for each num
                deduct this num from total -- diff
                half this diff
                check if this half is in hashmap
                    and that this half value isn't in the same index as current num
                if every condition is satisfied, update result value -- get max

        after going thru the array, max value is in result variable
    """
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums) # compute prefix sum

        # create hashmap that records the last index of a value
        hashmap = {v:i for i, v in enumerate(nums)}

        # variable that gets the largest possible outlier
        res = float('-inf')

        # loop for each value in nums
        for i, n in enumerate(nums):
            # get the difference of total with current num
            target = total - n

            # if target is odd, continue to next num
            # the difference is always going to be even
            if target % 2:
                continue

            # get the half value, this is the sum of spcl nums
            half = target // 2

            # if half value is in hashmap & it's not the current value
            if half in hashmap and hashmap[half] != i:
                res = max(res, n) # update max value

        # return
        return res

