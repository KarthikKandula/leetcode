class Solution:
    """
    use backtracking to solve the problem

    create a helper function to implement recursive dfs
        input for function -- current index & total of current subset
        check if index is out of bounds or total greater than target
            return from function
        check if total equal to target
            append subset copy to result
            return from function
        
        we have two choices
        append current index to subset & carry operations
            make recursive function call for current index -- checking as many possible combinations for current index

        don't append current index to subset & carry operations -- also eliminates duplicates
            make recursive function call for next index
    
    once all possibilities are explored, all combinations are in result array, return it
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # result array

        subset = [] # create a subset variable that keeps track of all current values
        # create hepler function to implement recursive function
        def dfs(i, total): # pass index, total of current subset
            # check if i is out of bounds or total > target
            if i >= len(candidates) or total > target:
                return # reached a dead end, return

            # check if target == total -- we've found one of the sets
            if target == total:
                res.append(subset.copy()) # append a copy of subset to result
                return

            # add current position to subset
            subset.append(candidates[i])
            dfs(i, total + candidates[i]) # recursive call to check with current position again & updated total

            subset.pop() #cleanup -- for checking without current position
            # add next position to subset
            dfs(i + 1, total) # recursive call to check with next position

        # initial function call
        dfs(0, 0)

        return res # return result array
