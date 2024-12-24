class Solution:
    """
    Optimized solution

    solve this problem using a single-pass two-pointer approach
        the goal is to remove all occurrences of a given value from the array
        use one pointer to iterate through the array
            this pointer checks each element
        use another pointer to track the position where the next valid (non-val) element should go
            this ensures all valid elements are shifted to the front of the array
        for each element, if it is not equal to the target value:
            copy it to the position of the second pointer
            increment the second pointer
        return the value of the second pointer, which indicates the length of the array without the target value
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        # variable to track the next non-val index
        # top replace any non-val value with, so that all val vals are towards the end
        index = 0

        # loop for every index of nums
        for i in range(len(nums)):
            # if current nums val is not equal to val, replace it at the non-val index in index
            if nums[i] != val: # valid/process
                nums[index] = nums[i] # replace value
                index += 1 # increment index

        # return index value
        return index

    """
    My solution
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        # create two pointers at either end of array
        i, j = 0, len(nums) - 1

        # another pointer to track length of nums
        k = len(nums)

        # loop while i is less than j
        while i < j:
            # advance j pointer until a value other than val is seen
            while i < j and nums[j] == val:
                j -= 1
                k -= 1

            # advance i pointer until val is seen
            while i < j and nums[i] != val:
                i += 1
        
            # if loop logic is broken, break the loop
            if not i < j:
                break

            # at this point, i -> val & j at non val
            # exchange values
            nums[i], nums[j] = nums[j], nums[i]
            k -= 1 # decrement k value since a val is processed

            # increment/decrement pointers
            i += 1
            j -= 1

        # Handle the edge case where i == j
        if i == j and nums[i] == val:
            k -= 1 # decrement k val since a val is processed

        return k
