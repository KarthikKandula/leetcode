class Solution:
    """
    Use binary search to solve the problem
        basic implementation of binary search with a slight twist

    as mentioned in the problem, the array is rotated, so a part of the array is sorted, there is a difference at a single point, which we need to find.
        use the formula left pointer value <= mid value
            if it is left subarray is sorted, search in right subarray
        if not
            right subarray is sorted, search in left subarray

    loop while left pointer <= right pointer
        calculate mid value
            replace if this is min value in result variable
        check if left pointer value <= mid value
            if it is left subarray is sorted, search in right subarray
        if not
            right subarray is sorted, search in left subarray

    loop thru end & answer is in result variable
    """
    def findMin(self, nums: List[int]) -> int:
        # left & right pointers - on either side of the input
        l, r = 0, len(nums) - 1
        res = nums[0] # set result to any random number in the input

        # basic binary search loop condition
        while l <= r:
            # check if left pointer < right pointer - if it is, we found the result update result with left pointer value
            if nums[l] < nums[r]:
                res = min(res, nums[l]) # replace result with minimum value, since left pointer value is less, it can be the min value in input
                break # we don't have to check for anymore conditions, break the loop

            # calculate mid value 
            mid = (l + r) // 2
            res = min(res, nums[mid]) # replace result with minimum value, if mid is the lowest value

            # check if left pointer value is less than mid value, if it is left subarray is sorted, search in right subarray
            if nums[l] <= nums[mid]:
                l = mid + 1 # increment left pointer
            else:
                r = mid - 1 # decrement right pointer

        # return result
        return res