class Solution:
    """
    O(1) space solution

    the idea for a constant space solution is to
        if we observe any example after the array is rotated we observe a pattern
        reverse the entire array
        reverse k elements (first k values)
        reverse n - k elements (last remaining values after k)
    
        also another thing to note is that k can be potentially reduced if we mod it with length of input

    if we do this we'll end up with the rotated array
    """
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) # get length of input
        k = k % n # mod k with length of input -- to account for k > n

        # reverse entire array
        l, r = 0, n - 1 # left & right pointers at either ends
        # loop while left is less than right
        while l < r:
            # replace num locations
            nums[l], nums[r] = nums[r], nums[l]

            # increment/decrement pointers
            l += 1
            r -= 1

        # reverse first k places
        l, r = 0, k - 1 # left & right pointers at either ends
        # loop while left is less than right
        while l < r:
            # replace num locations
            nums[l], nums[r] = nums[r], nums[l]

            # increment/decrement pointers
            l += 1
            r -= 1

        # reverse remaining places
        l, r = k, n - 1 # left & right pointers at either ends
        # loop while left is less than right
        while l < r:
            # replace num locations
            nums[l], nums[r] = nums[r], nums[l]

            # increment/decrement pointers
            l += 1
            r -= 1

    """
    O(N) space solution

    moving a value to the next k digits & storing the value at target in a hashmap
    doing this solves the problem but also uses O(N) space since hashmap can have all the values
    """
    # def rotate(self, nums: List[int], k: int) -> None:
    #     # create a hashmap with all values
    #     hashmap = {i:v for i, v in enumerate(nums)}

    #     n = len(nums) # get length of input

    #     # loop thru input nums
    #     for i, v in enumerate(nums):
    #         newIndex = i + k # calculate new index

    #         # if current index in hashmap, get value from hashmap
    #         if i in hashmap:
    #             v = hashmap[i]

    #         # if new index is less than length of input
    #         if newIndex < n:
    #             # backup value in hashmap
    #             hashmap[newIndex] = nums[newIndex]
    #             # swap can be made
    #             nums[newIndex] = v
    #         else:
    #             # if new index is greater than n, reduce it by n to get the actual index to move
    #             while newIndex >= n:
    #                 newIndex -= n
    #             # backup value in hashmap
    #             hashmap[newIndex] = nums[newIndex]
    #             # swap to be made now
    #             nums[newIndex] = v
