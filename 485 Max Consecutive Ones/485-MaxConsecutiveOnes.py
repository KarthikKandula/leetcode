class Solution:
    """
    Slightly optimal solution
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # variables for tracking count & max count
        count, maxCount = 0, 0

        # loop thru each value in nums
        for n in nums:
            # if current num is 1
            if n == 1:
                # increment count
                count += 1
            else:
                # encountered a 0, get the max count till now
                maxCount = max(maxCount, count)
                # reset count value to 0
                count = 0
        
        # get max one more time, to process if last value is 1
        return max(maxCount, count)

    """
    My solution
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0 # left pointer
        maxLen = 0 # max length of 1s

        # loop thru input using right pointer
        for r in range(len(nums)):
            # if current num is 1
            if nums[r] == 1:
                # compute max length for the current window
                maxLen = max(maxLen, (r - l) + 1)
            else:
                # encountered a 0, reset left pointer to next value -- possible start of a 1
                l = r + 1
        
        # return max length
        return maxLen
