# 40. Combination Sum II

1 possible solution for this problem  

## Method 1

We can solve this problem using a stack combined with a backtracking technique. This approach explores all possible subsets by making recursive calls based on two key conditions. It efficiently handles duplicate values to avoid generating redundant subsets.

### Steps

1. **Concept Overview**:
   - The problem revolves around two key conditions:
     1. **Adding the current index** to the stack and making a recursive call to explore possibilities including this index.
     2. **Skipping the current index** and making a recursive call to explore possibilities excluding this index.

2. **Recursive Function**:
   - In each recursive call:
     - **Add the current index value** to the stack and recursively call the function to explore further with this value included.
     - **Remove the current index value** from the stack after the recursive call to backtrack and explore other paths.
     - **Make another recursive call** without adding the current index value to explore paths that exclude it.

3. **Boundary and Target Conditions**:
   - In every recursive call, check the following:
     - **Out of Bounds**: If the index exceeds the array length, return from the function.
     - **Total Exceeds Target**: If the running total exceeds the target, return from the function.
     - **Total Equals Target**: If the running total equals the target, append a copy of the current subset to the result array and return.

4. **Handling Duplicates**:
   - Since the problem can contain duplicate values, **sort the input array** before starting the recursive process.
   - After adding a value at the current index to the stack, skip over all consecutive duplicate values by checking if the current value is equal to the next. Continue until a unique value is found, then proceed with the next recursive call.

5. **Efficiency with the Stack**:
   - By immediately adding and removing elements, the same stack can be reused across different recursive paths, minimizing memory usage.

6. **Exploring All Possibilities**:
   - The recursive function, by branching into two paths (including and excluding the current index), covers all possible subsets. It effectively avoids redundant subsets by skipping duplicates.

### Conclusion

This approach efficiently uses a stack and backtracking technique to explore all potential subsets while handling duplicates. By sorting the input array and skipping over consecutive duplicates, the solution ensures that only unique subsets are generated.


### Self Notes
We can use stack with backtracking to solve the problem in an effective manner. in backtracking we'll use recursive function to explore all possibilites. The entire problem depends on 2 conditions, 1. add current index to stack & recursive call for current index again to explore all possibilites 2. not adding current index value to stack, recursive call for next index to explore all possibilitis. By adding & cleaning up the stack immediately, we can keep using the same stack for other possiblities as well. in any particular function call, if one condition has been explored, it also explores other possibiltes as well, this is how all the possibilites are covered. Also in every function call check if index is out of bounds or total greater than target, return from function, check if total equal to target, append subset copy to result, return from function. Since this problem can contain duplicates, we have to find a way to skip duplicate sets. solution -- sort the array. after we add the current index, we skip all the values that are same i.e if current is equal to next until we find a unique value & then go on with the second condition.

```
"""
   use backtracking to solve the problem
      an issue arises with duplicate values where the same subset gets generated
      a possible way to avoid this is to sort the input array
         avoid all values that are same after processing first value
         this way we avoid duplicates

   create a helper function to implement recursive dfs
      input for function -- current index & total of current subset
      check if total equal to target
         append subset copy to result
         return from function
      check if index is out of bounds or total greater than target
         return from function
      
      we have two choices
      append current index to subset & carry operations
         make recursive function call for next index

      pop recently added value to subset -- wiping the slate clean to explore further possibilities

      skip all values are same as current 
         while loop to check if next value is same as current
         increment index if it is

      don't append current index to subset & carry operations -- eliminates duplicates
         make recursive function call for next index
   
   once all possibilities are explored, all combinations are in result array, return it
"""
```
