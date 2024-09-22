# 20. Valid Parentheses

1 possible solution for this problem  

## Method 1

We can solve this problem efficiently using a **stack**:

1. **Use a stack for opening braces**:
   - As we iterate through the string, push every opening brace (`'('`, `'{'`, `'['`) onto the stack.
2. **Match closing braces**:
   - When encountering a closing brace (`')'`, `'}'`, `']'`), check if it matches the top value in the stack:
     - If it does, pop the top element from the stack and continue.
     - If it doesn't match or the stack is empty, the string is invalid, and we return false.
3. **Edge case - leftover values**:
   - After processing the entire string, if there are still values in the stack, it means not all braces were closed, and the string is invalid.
4. **Final check**:
   - If the stack is empty at the end, it means all braces were properly matched, and the string is valid.

This approach ensures that all opening braces have corresponding closing braces, regardless of nesting.

### Self Notes
We can use stack to solve the problem in an effective manner. The problem is to find opening & closing braces in an order, every opening brace should have a closing based, doesn't matter how nested it is. to achieve this, we'll employ a strategy to add all opening braces to the stack & when we find a closing brace, we'll pop the last value in the stack to see if it's a matching closing brace, if it is, go on with validating rest of the values, if it isn't fail the testcase. Keep doing until the end to get the result. At the end, check if there are any values in the stack, if there are it means a brace wasn't closed - this is an edge case that should be covered. 

```
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
```
