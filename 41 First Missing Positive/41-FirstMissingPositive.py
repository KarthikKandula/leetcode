class Solution:
    """
    this problem can be implemented using cyclic sort algorithm
        cyclic sort is used to sort values in an array
        we use cyclic sort to place values in their respective places
        go thru the array again to find the first value that isn't in place
            so that index value is the smallest positive integer that isn't present in nums
        
    the intuition is as below
        we need to find the smallest +ve integer not in nums
        so possible values in nums are from 1...n
            we only need to check these values
        due to the way indexes work in programming
            for each index -- value should be index + 1
            for each value -- it should be in index value - 1
        so after implementing cyclic sort, all values need to be in their places aka above logic
            the first index that violates this logic, is the missing nubmer
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        # function to implement swap operation
        def swap(arr, i, j):
            # swap values
            arr[i], arr[j] = arr[j], arr[i]
        
        # get length of input
        n = len(nums)

        # loop for length of input, to sort values into their place using cyclic sort
        for i in range(n):
            # loop while value in this location is in range 1...n
            # and if the value isn't equal to nums[i] - 1 index
            while 0 < nums[i] <= n and nums[i] !=  nums[nums[i] - 1]:
                # if above condition satisfies, swap numbers
                swap(nums, i, nums[i] - 1)
        
        # loop for length of input, to find the fist value that isn't in place
        for i in range(n):
            # check if value in this index is equal to index + 1
            if nums[i] != i + 1:
                return i + 1 # if not, return i + 1, it's missing
        
        # if return isn't triggered above, return n + 1, since that's the lowest possible integer
        return n + 1

    """
    Convert input array into set & make comparisions
        update logic to check between 1...n
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        nums = set(nums)

        for i in range(1, n + 2):
            if i in nums:
                continue

            return i

    """
    First attempt & solve
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        minVal = min(nums)
        maxVal = max(nums)

        nums = set(nums)

        if minVal <= 0 and maxVal <= 0:
            return 1
        if minVal > 0 and minVal != 1:
            return 1
        if minVal <= 0:
            minVal = 1

        for i in range(minVal, maxVal + 2):
            if i in nums:
                continue

            return i


