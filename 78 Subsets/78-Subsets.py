class Solution:
    """
    Use backtracking to solve the problem

    create a hepler function that will be called recursively
        input for this function is current index on which ops are performed
        check if index is out of bounds
            append subset to result 
            return from function

        append current index to subset -- we're choosing to add current index
            make recursive function call for next index
        
        pop recently appended value to subset -- wiping the slate clean to explore further possibilites, not adding current index
            make recursive function call for next index
    
    once all possibilites are explored, all combinations are in result array
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # array to store outputs
        res = []

        # array to keep track of values in processing
        subset = []

        # helper function to implement recursive backtracking
        def dfs(i):
            # check if i is out of bounds
            if i >= len(nums):
                res.append(subset.copy()) # append a copy of subset to result -- we've exhausted all current possibilities
                return # return from function

            # decision point -- to include nums[i]
            # append current index to subset
            subset.append(nums[i])
            dfs(i + 1) # recursive call for next index

            # decision point -- to not include nums[i]
            subset.pop() # pop recently inserted value -- restore state of subset to the state it was in before the append
            dfs(i + 1) # recursive call for next index -- without inserting current index
        
        dfs(0) # initial call with first index

        # return result array
        return res
