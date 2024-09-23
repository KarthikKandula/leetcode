# 22. Generate Parentheses

1 possible solution for this problem  

## Method 1

We can solve this problem using a **stack** with a **backtracking** approach, leveraging recursion to explore all possible combinations.

1. **Base case**:
   - If `openCount == closeCount == n`, the current iteration ends, and the final valid string (from the stack) is recorded.
2. **Recursive conditions**:
   - If `openCount < n`: You can add an opening brace `'('` to the stack and recursively call the function with `openCount` incremented.
   - If `closeCount < openCount`: You can add a closing brace `')'` to the stack and recursively call the function with `closeCount` incremented.
3. **Reusing the stack**:
   - By immediately cleaning up the stack after each recursive call, the same stack can be reused for other possible combinations.
4. **Exploring all possibilities**:
   - Since each condition is evaluated independently (using `if` statements), multiple conditions can be satisfied in a single function call, allowing the recursive function to explore all valid combinations of parentheses.

This backtracking approach ensures that all valid combinations are generated efficiently by leveraging recursive exploration with stack manipulation.

### Self Notes
We can use stack with backtracking to solve the problem in an effective manner. in backtracking we'll use recursive function to solve it. The entire problem depends on 3 conditions, 1.  if openCount == closecount == n -> end current iteration, final string formed in stack, 2. if openCount <  n -> can add opening brace '(' to the stack, 3. if closecount <  openCount -> can add closing brace ')' to the stack. By adding & cleaning up the stack immediately, we can keep using the same stack for other possiblities as well. since all three conditions are if statements, in any particular function call. if one statement is satisfied, there is a possiblity of the other statement to also be satisfied, this is how all the possibilites are covered.

```
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
```
