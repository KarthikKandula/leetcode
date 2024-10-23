# 39. Combination Sum

1 possible solution for this problem  

## Method 1

We can solve this problem using a stack combined with a backtracking technique. The backtracking approach explores all possible subsets by making recursive calls based on two key conditions.

### Steps

1. **Concept Overview**:
   - The approach involves a recursive function to explore all possibilities:
     1. **Adding the current index** to the stack and making a recursive call with the same index to explore all combinations that include it.
     2. **Not adding the current index** to the stack and making a recursive call with the next index to explore combinations that exclude it.

2. **Recursive Function**:
   - In each recursive call:
     - **Add the current index value** to the stack and call the recursive function again with the same index.
     - After the recursive call, **remove the current index value** from the stack to backtrack and explore other paths.
     - Make another recursive call without adding the current index to explore combinations that exclude it.

3. **Boundary Conditions**:
   - In every recursive call, check for the following:
     - **Index Out of Bounds**: If the index exceeds the array length, return from the function.
     - **Total Exceeds Target**: If the total value in the stack exceeds the target, return from the function.
     - **Total Equals Target**: If the total equals the target, append a copy of the stack to the result and return.

4. **Efficiency with the Stack**:
   - By adding and removing elements immediately in the stack, we keep the stack reusable for other recursive paths. This dynamic update minimizes memory usage.

5. **Covering All Possibilities**:
   - The recursive function, by branching at each step, explores both conditions (inclusion and exclusion), ensuring all possible subsets are covered.

### Conclusion

This approach effectively uses a stack and backtracking to explore all potential combinations by leveraging recursive branching. The stack cleanup after each recursive call allows the same stack to be reused efficiently, reducing memory overhead while covering all valid subsets.


### Self Notes
We can use stack with backtracking to solve the problem in an effective manner. in backtracking we'll use recursive function to explore all possibilites. The entire problem depends on 2 conditions, 1. add current index to stack & recursive call for current index again to explore all possibilites 2. not adding current index value to stack, recursive call for next index to explore all possibilitis. By adding & cleaning up the stack immediately, we can keep using the same stack for other possiblities as well. in any particular function call, if one condition has been explored, it also explores other possibiltes as well, this is how all the possibilites are covered. Also in every function call check if index is out of bounds or total greater than target, return from function, check if total equal to target, append subset copy to result, return from function

```
"""
   use backtracking to solve the problem

   create a helper function to implement recursive dfs
      input for function -- current index & total of current subset
      check if index is out of bounds or total greater than target
         return from function
      check if total equal to target
         append subset copy to result
         return from function
      
      we have two choices
      append current index to subset & carry operations
         make recursive function call for current index -- checking as many possible combinations for current index

      don't append current index to subset & carry operations -- also eliminates duplicates
         make recursive function call for next index
   
   once all possibilities are explored, all combinations are in result array, return it
"""
```
