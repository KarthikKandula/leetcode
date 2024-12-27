class Solution:
    """
    can solve this problem using two pointers with a twist
        the idea is to know how many times a value appears in the input
            looping thru that many times to place the value in left pointers location
    
    take two pointers left & right at the beginning
    loop while right pointer is less than length of input
        get count of the current value right is pointing at
            initialize a variable count with value 1, since every value appears atleast once
            loop while right value is same as next value
                increment count
        by the above loops end, we get count of the current right pointer value
            and right is pointing at the end of that value
        loop again for the min of (2, count)
            to make sure 1's are accounted & loop is not more than twice
            place right pointers value (pointing to the last occurence of current value) in left pointers location
            increment left pointer
        by the end of above loop, current value is taken care of
        increment right pointer value to point at the next unique value
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        # left & right pointers at same location
        l, r = 0, 0

        # loop while right is less than length of input
        while r < len(nums):
            count = 1

            # get count of current right pointer value
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            count = min(2, count)

            # move right pointer value to left pointer location
            for i in range(count):
                nums[l] = nums[r]
                l += 1

            # increment right pointer
            r += 1
        
        return l
