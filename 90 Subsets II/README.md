# 90. Subsets II

1 possible solution for this problem  

## Method 1

We can solve this problem using a stack combined with a backtracking technique. The backtracking approach explores all possible subsets by making recursive calls based on two key conditions. To handle duplicates effectively, the solution involves sorting the input array.

### Steps

1. **Concept Overview**:
   - The approach uses a recursive function to explore all possibilities by branching into two key conditions at each step:
     1. **Adding the current index** to the stack and recursively exploring from the next index.
     2. **Skipping the current index** without adding it to the stack, recursively exploring from the next index.

2. **Handling Duplicates**:
   - Since the problem can involve duplicate values, the solution starts by **sorting the input array**. This allows us to efficiently skip over consecutive duplicate values in the recursive calls.
   - After adding a value at the current index to the stack, if the next value is the same as the current, we **skip over all duplicates** to avoid exploring redundant sets.

3. **Recursive Function**:
   - In each recursive call:
     - **Add the current index value** to the stack.
     - Call the recursive function with the next index to explore further with this value included.
     - After the recursive call, **remove the current index value** from the stack to backtrack and explore other paths.
     - **Skip all duplicate values** by checking if the current value is equal to the next one, and move to the next unique value.

4. **Exploring All Possibilities**:
   - The recursive function, by branching into two conditions (including and excluding values), explores all possible subsets efficiently.
   - By skipping duplicates during exploration, the function avoids redundant subsets.

5. **Efficiency with the Stack**:
   - By adding and removing elements immediately, the same stack is reused across different recursive paths, minimizing memory usage.

### Conclusion

This approach efficiently uses a stack and backtracking to explore all potential subsets while handling duplicate values. By sorting the input and skipping over consecutive duplicates, we ensure that only unique subsets are generated.


### Self Notes
We can use stack with backtracking to solve the problem in an effective manner. in backtracking we'll use recursive function to explore all possibilites. The entire problem depends on 2 conditions, 1. we're adding current index to stack 2. not adding current index value to stack. By adding & cleaning up the stack immediately, we can keep using the same stack for other possiblities as well. Since this problem can contain duplicates, we have to find a way to skip duplicate sets. solution -- sort the array. after we add the current index, we skip all the values that are same i.e if current is equal to next until we find a unique value & then go on with the second condition. This way we avoid duplicates. in any particular function call, if one condition has been explored, it also explores other possibiltes as well, this is how all the possibilites are covered.

```
"""
   Use backtracking to solve the problem
      an issue arises with duplicate values where the same subset gets generated
      a possible way to avoid this is to sort the input array
         avoid all values that are same after processing first value
         this way we avoid duplicates

   create a helper function that will be called recursively
      input for this function is current index on which ops are performed
      check if index is out of bounds
         append subset to result
         return from function
      
      append current index to subset -- choosing to add current index
         make recursive function call to next index
      
      pop recently added value to subset -- wiping the slate clean to explore further possibilities

      skip all values are same as current 
         while loop to check if next value is same as current
         increment index if it is
      
      make recursive function call for next index -- choosing to not add current index

   once all possibilites are explored, all combinations are in result array
"""
```
