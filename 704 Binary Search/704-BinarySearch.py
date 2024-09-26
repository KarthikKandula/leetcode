class Solution:
    """
        Iterative solution
    """
    def search(self, nums: List[int], target: int) -> int:
        # Create left & right pointers
        l, r = 0, len(nums)-1

        # Loop while left <= right
        while l <= r:
            # Find mid point using left & right pointers
            mid = (l+r)//2

            # If target > mid 
            if target > nums[mid]:
                l = mid+1 # increment left pointer to mid+1 - cutting the input array to half
            # If target < mid 
            elif target < nums[mid]:
                r = mid-1 # increment right pointer to mid-1 - cutting the input array to half
            # If target == mid
            else:
                return mid # return mid i.e index

        # return -1 if matches were not found
        return -1

    """
        Recursive Solution
    """
    # def search(self, nums: List[int], target: int) -> int:
    #     # create nested function to implement recursive binary search solution
    #     def binSearch(start, end) -> int:
    #         # base condition for recursive function
    #         if start > end: # if start > end, it means element isn't present in the current input
    #             return -1 # return false value
            
    #         # Find mid point using start & end pointers
    #         mid = (start + end) // 2

    #         # If mid > target - means target value in left subarray 
    #         if nums[mid] > target:
    #             # recursive function call - returns int, need to return it
    #             return binSearch(start, mid - 1)
    #         # If mid < target - means target value in right subarray 
    #         elif nums[mid] < target:
    #             # recursive function call - returns int, need to return it
    #             return binSearch(mid + 1, end)
    #         else: # if reaches this position, we've found the value
    #             return mid # return index value, that is the ask
        
    #     # first function call, with start & end values
    #     return binSearch(0, len(nums)-1)

