class Solution:
    """
    neetcode solution

    use backtracking to solve the problem
        need to compile all possible combinations to generate all possible strings
    
    create a helper function that is implemented recursively
        input to this function is current index in input & current string
        check if length of current string is equal to length of digits -- base case
            append current string to result array -- found a candidate
            return from function
        loop thru all the letters at that digit (retrieve from hashmap)
            recursively call for next index along with updated curr string
        since we don't need to do this is a list of list manner, don't have to clean current string for future operations
            usually a constant in backtracking problems but not required in this
    
    once all recursive ops are done, result is in the result array, return it
    """
    def letterCombinations(self, digits: str) -> List[str]:
        # check if digits is empty
        if not digits:
            return [] # return empty string
        
        # result array
        res = []
        # hashmap for base values
        hashmap = {2:'abc', 3:'def', 4:'ghi', 5: 'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

        # helper function for implementing recursive backtracking
        def backtracking(i, currStr):
            # if length of current string is equal to length of input digits -- means we found a candidate
            if len(currStr) == len(digits):
                res.append(currStr) # append current string to result
                return # return from function
            
            # loop for input strings in current position in digits
            for char in hashmap[int(digits[i])]:
                # recursive function call for next index & updated current string
                backtracking(i + 1, currStr + char)
        
        # initial recursive function call
        backtracking(0, '')

        # return result string
        return res

    """
    my solution

    loop thru input digits, one by one 
    create helper function that takes all available combinations in stack & loop thru new digits, in a double loop
        append all combinations to stack -- replace old values with new values
    once this is done for all values in digit, return stack -- all values are in it
    """
    def letterCombinations(self, digits: str) -> List[str]:
        self.stack = [] # create an array that holds the values

        # hashmap for base values
        hashmap = {2:'abc', 3:'def', 4:'ghi', 5: 'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

        # helper function for implementing logic
        def backtracking(digi):
            tempStack = [] # create a temp stack

            # if stack is empty -- to initialize values for first digit
            if not self.stack:
                for j in digi: # loop thru values in digi
                    tempStack.append(j) # append to tempStack

            # loop thru values in stack
            for i in self.stack:
                for j in digi: # loop thru values in digi
                    tempStack.append(i + j) # append to tempStack

            self.stack = tempStack # replace values in stack with values in tempStack, since values are updated

        # loop to call helper function for each digit
        for l in digits:
            backtracking(hashmap[int(l)])
        
        # return stack
        return self.stack