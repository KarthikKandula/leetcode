class Solution:
    """
    Use stack with backtracking to solve the problem

    create a nested function that will be called recursively
        for a string to be valid it has to have n no. of opening & closing braces
            this will be tracked using the openCount & closeCount
        3 primary conditions will be tested 
            1. if openCount == closecount == n -> end current iteration, final string formed in stack
            2. if openCount <  n -> can add opening brace '(' to the stack
            3. if closecount <  openCount -> can add closing brace ')' to the stack
        
        since all three conditions are if statements, in any particular function call 
            if one statement is satisfied, there is a possiblity of the other statement to also be satisfied
                this is how all the possibilites are covered.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # create stack to keep track of braces
        res = [] # result variable 

        # use backtracking using recursion
        # function to call recursively - inputs are open count & close count
        def backtracking(openCount, closeCount):
            # 1st condition - if open count & close count == n, that's the end of current string
            if openCount == closeCount == n:
                res.append("".join(stack)) # join all values in stack to get final result
                return # end current recursive iteration
            
            # 2nd condition - if open count < n - can add an opening brace
            if openCount < n:
                stack.append('(') # append an opening brace to the stack
                backtracking(openCount + 1, closeCount) # recursively call function by updating the open count
                stack.pop() # pop recently inserted opening brace - kind of like cleanup for future possibilities

            # 3rd condition - if close count < open count - can add a closing brace
            if closeCount < openCount:
                stack.append(')') # append an opening brace to the stack
                backtracking(openCount, closeCount + 1) # recursively call function by updating the close count
                stack.pop() # pop recently inserted closing brace - kind of like cleanup for future possibilities
        
        # initial call to backtracking function
        backtracking(0, 0)

        # return result variable, contains the result
        return res
