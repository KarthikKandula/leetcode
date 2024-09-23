class Solution:
    """
    Use stack to solve the problem

    Initialize a stack & loop thru the input string
        check if the current char is one of +, -, *, / (any operators)
            pop the last two chars, since we need two values to perform any arithmetic operations
                perform the arithmetic operations & append result to stack - to be used in future ops
        if it's a numeric, append to stack
    
    In the end final result is still in stack, only value at that point, return it for answer
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # Create stack to keep track of elements

        # Iterate through input tokens
        for i in tokens:
            # Check if current value is any of the operators - operations in the below work like this a + b = c
            if i == '+':
                b, a = stack.pop(), stack.pop() # pop latest & second latest value from stack
                stack.append(a + b) # perform operations based on sign
            elif i == '-':
                b, a = stack.pop(), stack.pop() # pop latest & second latest value from stack
                stack.append(a - b) # perform operations based on sign
            elif i == '*':
                b, a = stack.pop(), stack.pop() # pop latest & second latest value from stack
                stack.append(a * b) # perform operations based on sign
            elif i == '/':
                b, a = stack.pop(), stack.pop() # pop latest & second latest value from stack
                stack.append(int(a / b)) # perform operations based on sign
            else:
                # If c is not an operators, append to stack since it's numeric
                stack.append(int(i))

        # final result if also stored in stack, by this point should only have one value
        return stack[0]
