class Solution:
    """
    This is a basic sliding window problem
        our objective is to find the max no. of 1's after replacing 0's
        for this we need to track the no. of replaced 0's
        if the max number is exceed, shrink the window & keep going until reaches the end
        calculate the window size frequently
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        # varibles to track replaces 0's and max count until now
        replaced = 0
        maxCount = 0

        l = 0 # left pointer

        # loop thru input using right pointer
        for r in range(len(nums)):
            # if curr is 0, -- replaced + 1
            if nums[r] == 0:
                replaced += 1

            # if replaced is >= k, shrink window -- reduce l until replace is <= k
            while replaced > k:
                if nums[l] == 0:
                    replaced -= 1
                
                l += 1

            # get current window
            maxCount = max(maxCount, (r - l) + 1)

        return maxCount
