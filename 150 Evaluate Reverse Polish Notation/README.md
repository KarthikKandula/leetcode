# 150. Evaluate Reverse Polish Notation

1 possible solution for this problem  

## Method 1

We can solve this problem using a **stack** to handle arithmetic operations in the given order:

1. **Use a stack**:
   - Traverse the expression token by token.
   - If the token is a number, push it onto the stack.
2. **Handle operators**:
   - When an arithmetic operator (`+`, `-`, `*`, `/`) is encountered, pop the top two values from the stack.
   - Perform the operation: `second operand operator first operand` (since the second value popped is the first operand in the expression).
   - Push the result back onto the stack to be used in future operations.
3. **Handle numeric values**:
   - If encountered a numeric value, push value into the stack
4. **Continue until the end**:
   - Repeat this process for each token in the expression.
5. **Final result**:
   - After processing all tokens, the final value left in the stack is the result of the entire expression. Return this value as the solution.

This approach effectively processes arithmetic expressions by maintaining intermediate results in the stack.

### Self Notes
We can use stack to solve the problem in an effective manner. The problem is to perform arithmetic operations in the order given. If you find any arithmetic operator (+, -, *, /), pop two values in the stack & perform said operation on them, add the result back to the stack since we need that value to perform additional operations in future. If you find any number instead, add it to the stack. Keep doing it until the end & the final result is in the stack, return the value & it's a success.

```
"""
    Use stack to solve the problem

    Initialize a stack & loop thru the input string
        check if the current char is one of +, -, *, / (any operators)
            pop the last two chars, since we need two values to perform any arithmetic operations
                perform the arithmetic operations & append result to stack - to be used in future ops
        if it's a numeric, append to stack

    In the end final result is still in stack, only value at that point, return it for answer
"""
```
