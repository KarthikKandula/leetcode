# 78. Subsets

1 possible solution for this problem  

## Method 1

To solve this problem, we use a combination of a stack and backtracking to explore all possible solutions effectively. The core idea is to recursively explore the inclusion and exclusion of each index in the stack.

### Steps

1. **Concept Overview**:
   - The solution involves backtracking to explore two choices at each step:
     1. **Adding** the current index value to the stack.
     2. **Not adding** the current index value to the stack.
   - By exploring both choices, we cover all possible combinations or solutions to the problem.

2. **Recursive Function**:
   - Define a recursive function to handle backtracking.
   - In each recursive call:
     - **Add the current index** value to the stack.
     - Call the function recursively to explore further with the updated stack.
     - **Remove** the current index value from the stack after the recursive call.
     - This "cleanup" step ensures that the stack remains reusable for other recursive paths.

3. **Exploring All Possibilities**:
   - For every index, the recursive function explores:
     - One branch where the value is included in the stack.
     - Another branch where the value is not included.
   - This exhaustive exploration guarantees that all possibilities are covered.

4. **Efficiency with the Stack**:
   - The stack is dynamically updated by adding and removing elements as we explore different paths.
   - This avoids creating unnecessary copies of the stack and optimizes memory usage.

### Conclusion

This approach efficiently uses a stack and backtracking to explore all possible combinations by leveraging recursive branching. The stack cleanup after each recursive call allows the same stack to be reused across different paths, minimizing memory overhead.

### Self Notes
We can use stack with backtracking to solve the problem in an effective manner. in backtracking we'll use recursive function to explore all possibilites. The entire problem depends on 2 conditions, 1. we're adding current index to stack 2. not adding current index value to stack. By adding & cleaning up the stack immediately, we can keep using the same stack for other possiblities as well. in any particular function call, if one condition has been explored, it also explores other possibiltes as well, this is how all the possibilites are covered.

```
"""
   Use backtracking to solve the problem

   create a hepler function that will be called recursively
      input for this function is current index on which ops are performed
      check if index is out of bounds
         append subset to result 
         return from function

      append current index to subset -- we're choosing to add current index
         make recursive function call for next index
      
      pop recently appended value to subset -- wiping the slate clean to explore further possibilites, not adding current index
         make recursive function call for next index

   once all possibilites are explored, all combinations are in result array
"""
```
