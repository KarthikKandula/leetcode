class Solution:
    """
    Use binary search to solve the problem
        basic implementation of binary search with a slight twist

    as mentioned in the problem, the array is rotated & we need to find an element in this array
        the key is to check if the left & right subarrays are sorted & if the target is in there
            if it is we search in that particular subarray
            if it isn't we search in the opposite subarray
    
    loop while left pointer <= right pointer
        calculate mid value
            if this is target, return mid index
        check if left pointer value <= mid value -- this means left subarray is sorted
            check if left value <= target <= mid value -- this is checking if the target is between these values
                if it is, check in left subarray
            if it isn't, value is in the right subarray, check in right subarray
        if the above condition is false -- it means right subarray is sorted
            check if mid value <= target <= right value -- this is checking if the target is between these values
                if it is, check in right subarray
            if it isn't, value is in the left subarray, check in left subarray

    loop until condition is invalidated & if result isn't returned in the loop, value isn't present in input
    """
    def search(self, nums: List[int], target: int) -> int:
        # left & right pointers for binary search
        l, r = 0, len(nums) - 1

        # basic binary search condition
        while l <= r:
            # calculate mid position
            mid = (l + r) // 2

            # check if mid == target, if it is found the index
            if nums[mid] == target:
                return mid # return found index

            # check if left value <= mid value, it means left subarray is sorted
            if nums[l] <= nums[mid]:
                # check if target is between l & mid
                if nums[l] <= target and target <= nums[mid]:
                    # check in left subarray
                    r = mid - 1
                else: # target is not between l & mid, search in right subarray
                    l = mid + 1
            else: # this means right subarray is sorted
                # check if target is between mid & r
                if nums[mid] <= target and target <= nums[r]:
                    # check in right subarray
                    l = mid + 1
                else: # target is not between mid & r, search in left subarray
                    r = mid - 1

        # target is not in input, return -1 as per problem desc
        return -1
