class Solution:
    """
    we can solve the problem using classic two pointer method with couple twists
        the jist of this problem is figuring out the middle portion of the array to remove
        to get that, we need to find increasing values starting with first element
            also find increasing value ending with last element
        now, once the increasing values have been found with the last element
            start from the first element and increase left pointer one by one as long as
                the left pointer is less than right pointer
                update mid subarray length (res variable) in each loop -- get min value
            if at any point, left value is greater, increment right pointer
            keep doing it until the end and the min subarray length is in the result variable
        this method works since, we're considering all possiblities
    """
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # get length of input
        n = len(arr)

        # get increasing order from right to left
        # create right pointer at end
        r = n - 1

        # loop while r isn't 0 and elements are in decreasing order (from last)
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1 # decrement r pointer
        
        # assign result to r -- case when all elements are in increasing order, this is going to be the result
        res = r

        # create left pointer at start
        l = 0

        # loop while left & right don't meet
        while l < r:
            # loop while right is in bounds and left pointer is greater than right pointer
            while r < n and arr[l] > arr[r]:
                r += 1 # increment right pointer 
            
            # update result window
            res = min (res, r - l - 1)
            # using r - l - 1 since need the no. of value elements in subarray

            # if at any point, we hit a decreasing value from beginning, it's the end of increasing values from beginning
            if arr[l] > arr[l + 1]:
                break
            
            # increment left pointer -- in normal loops
            l += 1
        
        # return result in the end
        return res
