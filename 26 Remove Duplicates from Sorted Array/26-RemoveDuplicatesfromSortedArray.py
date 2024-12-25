class Solution:
    """
    Other solution -- same time & space

    this is same as my solution but with different code & slightly tweaked approach
        this approach always keeps track of the location to update next with left pointer
        the comparisions are made with right pointer & right - 1
            since there will be duplicates, this comparision also works to find unique values
        once a unique value has been found, replace it with left pointer location
            increment left pointer location
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # create left pointer at 1st index -- since 0th index is always sorted

        # loop thru length of nums from 1st index -- since 0th index is always going to be sorted
        for r in range(1, len(nums)):
            # check if right pointer value is different from r - 1 value
            # if it's different it means we've found a new unique value
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r] # update left pointer with right pointer value
                l += 1 # increment left pointer
        
        # return left pointer value
        return l

    """
    Own solution

    this solution always keeps track of the last unique value with the left pointer
        always compares the last unique pointer with right pointer
        once a new value is found
            we increment the left pointer first, to update the next variable
            and then update the value
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        # create left pointer
        l = 0

        # loop thru length of nums from 1st index -- since 0th index is always going to be sorted
        for r in range(1, len(nums)):
            # if left pointer value is less than right pointer val -- we've found a place to replace
            if nums[l] < nums[r]:
                l += 1 # increment left pointer value
                nums[l] = nums[r] # replace left pointer value with right pointer value
        
        # left pointer points at last unique value, since it's an index, we return + 1 to account for total length
        return l + 1
