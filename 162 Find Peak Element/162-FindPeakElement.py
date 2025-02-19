class Solution:
    """
    we can solve the problem using binary search (modified binary search)
        solving the problem in linear time is simple & easy
        but solving in O(log n) is challenging
        
        the important pieces of info that is useful for bin search is
            no two values are the same
            the ends are -inf, which means inside value is the higher value
        if we consider both these statements, we can deduce that
            a peak element is only followed by lesser numbers
            so when we find a mid point
                if the left value is higher, there is possiblity that a peak element exists on that side
                    even if no values exist on that side
                    we can conclude that if it's the end of array or there are only less values after that
                    that value will still be the peak element
                same with right value is higer
            so by going towards whatever is the higher value at every mid point
            we can find a peak element
    """
    def findPeakElement(self, nums: List[int]) -> int:
        # pointers for binary search
        l, r = 0, len(nums) - 1

        # basic binary search implementation
        while l <= r:
            # calculate mid point
            mid = (l + r) // 2

            # check if left is greater -- search left
            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            # check if right is greater -- search right
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            # if a value isn't less than left or right, it's a peak element, return the index
            else:
                # return index
                return mid
        
        # no need for return statement outside since result is guaranteed
