class Solution:
    """
    this is a dynamic programming problem
        at any possible moment, we're interacting with two indexes
            i - index of word1
            j - index of word2
        there are 3 possible values operations possible at any single location
            insert - (i, j + 1)
                we're inserting the value just before our i pointer in word1
                by performing this operation, we'll have to move j pointer since the word is matching
                i pointer still remains in same location since it has to be matched
            delete - (i + 1, j)
                we're deleting the value at i pointer in word1
                by performing this operation, move i pointer since letter from word1 is deleted, check next letter
                j pointer still remains in same location since it has to be matched
            replace - (i + 1, j + 1)
                we're replacing the value at i pointer to match with j
                since they're matching we can move both pointers
        at any time we're doing this operation we always get the min value since problem asks for min no. of operations
    """
    def minDistance(self, word1: str, word2: str) -> int:

        # get length of inputs in seperate variables
        m, n = len(word1), len(word2)

        # create cache for memoization
        cache = [[-1] * n for _ in range(m)]

        # helper function to implement recursively
        def dfs(i, j): # i - index of word1, j - index of word2
            # base conditions
            # if i reaches end -- return second word difference
            if i == len(word1):
                return n - j # return count of remaining letters from word2
            # if j reaches end -- return first word difference
            if j == len(word2):
                return m - i # return count of remaining letters from word1
            
            # check if this function has been called previously
            if cache[i][j] != -1:
                return cache[i][j] # return value from cache -- reduces function calls

            # check if current index values match
            if word1[i] == word2[j]:
                # func calls for next index for word1 & word2 cuz current index matches
                cache[i][j] = dfs(i + 1, j + 1) 
                return cache[i][j]
                # return dfs(i + 1, j + 1)
            
            # if doesn't match - check all possibilities
            # func calls for insert & delete operations -- get the min value
            res = min(dfs(i + 1, j), dfs(i, j + 1))
            # func calls for replace operations -- get min value for this & above func calls
            res = min(res, dfs(i + 1, j + 1))

            # add 1 to the lowest func return call value -- to account for this operation
            cache[i][j] = res + 1

            # return value from cache
            return cache[i][j]
            # return res + 1
        
        # initial function call
        return dfs(0, 0)