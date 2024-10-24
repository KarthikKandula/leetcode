class Solution:
    """
    Use backtracking to solve the problem
        an issue arises with duplicate values where the same subset gets generated
        a possible way to avoid this is to sort the input array
            avoid all values that are same after processing first value
            this way we avoid duplicates

    create a helper function that will be called recursively
        input for this function is current index on which ops are performed
        check if index is out of bounds
            append subset to result
            return from function
        
        append current index to subset -- choosing to add current index
            make recursive function call to next index
        
        pop recently added value to subset -- wiping the slate clean to explore further possibilities

        skip all values are same as current 
            while loop to check if next value is same as current
            increment index if it is
        
        make recursive function call for next index -- choosing to not add current index

    once all possibilites are explored, all combinations are in result array
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] # result array
        nums.sort() # sort nums

        # create array to keep track of current elements
        subset = []
        def backtracking(i):
            # check if i is out of bounds -- base case
            if i >= len(nums):
                res.append(subset.copy()) # append a copy of subset to result -- we found a possible result
                return
            
            # include current location nums
            subset.append(nums[i]) # append current location nums to subset
            backtracking(i + 1) # recursive function call for next index

            # cleanup subset -- for future ops
            subset.pop()

            # don't include current location nums
            # remove all duplicate values from consideration
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 # increment 1 if values are equal
            backtracking(i + 1) # recursive call for next index -- removing the current duplicate value as well

        # initial recursive function call with index 0
        backtracking(0)

        # return result array
        return res
