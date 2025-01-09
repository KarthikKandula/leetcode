class Solution:
    """
    we can solve this problem using two pointers
        use the left pointer to keep track of location where the next value goes
        loop thru the input array & place non zero values in left pointer location
        by the end, all 0's will be moved to end
    """
    def moveZeroes(self, nums: List[int]) -> None:
        # left pointer
        l = 0

        # loop thru input array using right pointer
        for r in range(len(nums)):
            # if right pointer value is a 0, skip to next value
            if nums[r] == 0:
                continue

            # if not, swap values with left pointer
            nums[r], nums[l] = nums[l], nums[r]
            
            l += 1 # increment left pointer

    """
    Extra Space solution
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # create a copy array
        copy = [0] * len(nums)

        # initialize pointer to track location in copy array
        j = 0

        # loop thru input
        for i in range(len(nums)):
            # if current value in input array is not 0
            if nums[i] != 0:
                # copy this value to copy array
                copy[j] = nums[i]
                j += 1 # increment j pointer
        
        nums = copy

