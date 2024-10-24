class Solution:
    """
    use backtracking to solve the problem
        an issue arises with duplicate values where the same subset gets generated
        a possible way to avoid this is to sort the input array
            avoid all values that are same after processing first value
            this way we avoid duplicates

    create a helper function to implement recursive dfs
        input for function -- current index & total of current subset
        check if total equal to target
            append subset copy to result
            return from function
        check if index is out of bounds or total greater than target
            return from function
        
        we have two choices
        append current index to subset & carry operations
            make recursive function call for next index

        pop recently added value to subset -- wiping the slate clean to explore further possibilities

        skip all values are same as current 
            while loop to check if next value is same as current
            increment index if it is

        don't append current index to subset & carry operations -- eliminates duplicates
            make recursive function call for next index
    
    once all possibilities are explored, all combinations are in result array, return it
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # result array
        candidates.sort() # sort input -- helps to avoid duplicates

        subset = [] # subset array to keep track of subset at any point

        # helper function to implement recursive backtracking
        def backtracking(i, total):
            # check if total equal to target
            if total == target:
                res.append(subset.copy()) # we found a subset -- append to result set
                return # return from function

            # check if i is out of bounds or total greater than target -- can't be a possible subset
            if i >= len(candidates) or total > target:
                return # return from function
            
            # include current value
            subset.append(candidates[i]) # append current value to subset
            backtracking(i + 1, total + candidates[i]) # recursive function call for next index & updated total

            # cleanup subset -- for future ops
            subset.pop()

            # don't include current value
            # check if next value is same -- don't include, can cause duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 # increment i to avoid duplicates

            # recursive function call for next index & same total - since didn't include current element
            backtracking(i + 1, total)

        # initial function call        
        backtracking(0, 0)

        # return result array
        return res
