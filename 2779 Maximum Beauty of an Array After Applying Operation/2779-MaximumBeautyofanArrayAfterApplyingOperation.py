class Solution:
    """
    the idea here to find the largest window within the array that satisfies the condition
        largest num - small num <= k * 2
            this is a mathematical formula that should satisfy for this problem
        sort the array so that
        sorting the array to simplify the problem
            after sorting, the difference between the largest and smallest numbers is simply - nums[r]−nums[l]

        so we start the problem with window starting at l, r
        as we move higher in the window, calculate if the condition is holding up
            if condition is broken, increment left pointer
        
        in the end, the length of the array where the condition holds up is the answer
            hence return r - l + 1, this is the window length
    """
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # sort input array
        nums.sort()

        # define left pointer
        l = 0

        # loop for the length of input nums -- this is the right pointer
        for r in range(len(nums)):
            # check if largest num - smallest num in the current window is greater than k * 2
            # if it is, this window is invalid, reduce window
            if nums[r] - nums[l] > k * 2:
                l += 1 # increment left pointer, this is reducing the window
        
        # return value of the answer
        return r - l + 1
