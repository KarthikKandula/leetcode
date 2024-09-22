class Solution:
    """
    Use stack to solve the problem

    Initialize a stack & loop thru the input string
        check if the current char is one of ), }, ] - we have to find a corresponding opening brace for it to be a valid string
            check if the stack if initialized - if it isnt means that this appeared before an opening string, meaning failure
                pop the last char, check if its a matching openeing char
                    if it is, go on with the rest of the string
                    if it isn't, test case is a failure
            if isn't initialized, fail the test case
        if it is one of the opening chars, append it to the stack
    
    In the end, check length of the stack, if there are values in stack it means one of the values isn't closed off
    """
    def isValid(self, s: str) -> bool:
        # Create a stack
        stack = []

        # Loop for every char in input s
        for c in s:
            # Check if c is one of ), }, ]
            if c == ')' or c == '}' or c == ']':
                # If stack is initialized, do comparision
                if stack:
                    # Pop last char from stack
                    v = stack.pop()
                    # Check if closed char corresponds to popped char from stack
                    if c == ')' and v != '(':
                        return False # If not return false
                    elif c == '}' and v != '{':
                        return False
                    elif c == ']' and v != '[':
                        return False
                else: # To avoid edge case of first character being closed brace
                    return False
            else: # If c is one of opening braces
                stack.append(c) # Append c to stack

        # return True if stack is empty, if it's not, it means there is a parantheses not closed 
        return True if not stack else False
