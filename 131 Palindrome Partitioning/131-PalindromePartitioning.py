class Solution:
    """
    use backtracking to solve the problem
        we need to check all the possible combinations of palindrome's without changing the order of the letters in string
        we need to recursively check if a certain string is palindrome for each index till end of string
    
    create a result array & an array to keep track of all subset partitions

    create a helper function that is implemented recursively
        input to this function is the index at which we're performing current operation
        check if index is out of bounds
            append subset to result -- we've found one possible candidate
            return from function
        in a loop for each index from index to end of string
            check if each combination is palindrome -- create a helper function
                if index is 1, end of string is 4
                    check for 1-2, 1-3, 1-4
                if any string is palindrome, append to subset
                recursively call for next index -- same thing happens in that function as well
                clean up subset for future operations
    
    once all recursive functions are done, result is in the array, return it
    """
    def partition(self, s: str) -> List[List[str]]:
        res = [] # result array

        # subset array to track values this iteration
        subsetPartition = []

        # helper function to implement recursive backtracking
        def backtracking(i):
            # check out of bounds
            # check if i is out of bounds
            if i >= len(s):
                res.append(subsetPartition.copy()) # if it is, append a copy of subset to result -- we found one possible result
                return # return from function
            
            # recursive function calls for every combination
            # loop for every index between i & end of string
            for j in range(i, len(s)):
                # check if string between i & j is a palindrome
                if self.isPalindrome(s, i, j):
                    subsetPartition.append(s[i:j+1]) # append to subset if it is a palindrome
                    backtracking(j + 1) # recursive call for next index
                    subsetPartition.pop() # cleanup subset -- for future iterations

        # initial recursive call with index 0
        backtracking(0)

        # return result array
        return res
    
    # helper function to implement palindrome functionality
    def isPalindrome(self, s, l, r):
        # while left is less than right
        while l < r:
            # check if left & right positions aren't equal
            if s[l] != s[r]:
                return False # return False -- don't have to look further
            l += 1 # increment left pointer
            r -= 1 # decrement right pointer

        # return True if False condition isn't hit above
        return True
