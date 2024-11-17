# 198. House Robber

1 possible solution for this problem  

## Method 1 (Recursive approach)

## Problem Intuition
The task is to determine the maximum amount of money you can rob from a row of houses, where adjacent houses cannot be robbed on the same night. This problem can be solved using dynamic programming by calculating the maximum amount at each house based on prior decisions.

Instead of using an array to store results for each house, this approach optimizes space by maintaining only two variables to track the previous maximum values.

## Approach

### Key Idea
1. **Dynamic Programming with Constant Space**:
   - Maintain two variables (`rob1` and `rob2`) to represent:
     - `rob1`: The maximum amount robbed up to the house two steps back.
     - `rob2`: The maximum amount robbed up to the previous house.
   - Update these variables as you iterate through the houses, keeping track of the maximum amount robbed at each step.

### Step-by-Step Solution

1. **Initialize Variables**:
   - Set `rob1` and `rob2` to `0`, representing the maximum amount robbed at the two initial positions before the first house.

2. **Iterate Through the Houses**:
   - For each house in the input array `nums`:
     - Calculate the maximum amount you can rob at this house as:
       ```plaintext
       temp = max(rob1 + n, rob2)
       ```
       - `rob1 + n`: Rob the current house, adding its value to the maximum amount robbed up to two houses back.
       - `rob2`: Skip the current house and keep the maximum amount robbed up to the previous house.
     - Update `rob1` and `rob2` for the next iteration:
       ```plaintext
       rob1 = rob2
       rob2 = temp
       ```

3. **Return the Result**:
   - After the loop, `rob2` contains the maximum amount that can be robbed without violating the adjacency constraint.

### Summary
- **Space Optimization**: By maintaining only two variables instead of a DP array, space complexity is reduced to `O(1)`.
- **Efficiency**:
  - **Time Complexity**: `O(n)`, as the algorithm iterates through the array once.
  - **Space Complexity**: `O(1)` due to constant space usage.
- **Output**: The maximum amount that can be robbed without triggering alarms is stored in `rob2`.


### Self Notes

```
Iterative approach
"""
   this approach implements a constant space to this dp problem
      what it's doing is effectively calculating the max possible value at each location
      saving these values to two values & keep moving along the array in one pass

   take two values initialized to 0

   loop for input nums
      calc the max of prev 1st index + current value & the prev value
         adding n to only the 1st value skipping immediate adjacent value
      assign rob2 to rob1 -- shifting values
      assign temp to rob2 -- shifting values done
   
   return rob2 at the end since the last value has max value
"""

Linear time memoization approach
"""
   Better memoization approach
      this approach is only making calls for the next two indexes
      it's only adding the current value to the 2nd index
         so it's effectively skipping adding current value to next 1st index

   this implements the same regular recursive approach but elimates a layer of recursive function calls

   take an array initialized to -1 for the length of input n
      -1 indicates this value isn't yet calculated
   
   now in a function call before making recursive calls
      check if the array has been initialized at this index
      if it is, return the value -- reducing the amount of function calls by reusing them effectively

   before returning, get the max value of the
      return value of next 1st index
      current value + return value of next 2nd index
"""

Exponential time memoization approach -- mine
"""
   My solution - 2^N run time

   2^N run time is happening since we're calling all the possible values skipping the next value
      since there are multiple calls happening for each index, it's 2^N
"""
```
