# 213. House Robber II

1 possible solution for this problem  

## Method 1

## Problem Intuition
The task is to determine the maximum amount of money you can rob from a circular row of houses, where adjacent houses (including the first and last) cannot be robbed on the same night. This problem extends **House Robber I** with the added complexity of the circular constraint.

The circular condition can be simplified by splitting the problem into two cases:
1. Rob houses **excluding the last house** (include the first house).
2. Rob houses **excluding the first house** (include the last house).

The result is the maximum value obtained from these two cases.

## Approach

### Key Idea
1. **Split the Problem**:
   - Solve the problem twice:
     - Once for the array excluding the last house.
     - Once for the array excluding the first house.
   - Return the maximum of the two results.
2. **Reuse the House Robber I Solution**:
   - Use the constant space dynamic programming approach from **House Robber I** to calculate the maximum value for each case.

### Step-by-Step Solution

1. **Handle Edge Cases**:
   - If the input `nums` has only one house, return `nums[0]` directly as there’s no circular constraint to consider.

2. **Define a Helper Function for House Robber I**:
   - Implement the space-optimized solution for **House Robber I**:
     - Maintain two variables (`rob1` and `rob2`) to track the maximum amount robbed up to two houses back (`rob1`) and the previous house (`rob2`).
     - Iterate through the houses and update these values:
       ```plaintext
       temp = max(rob1 + n, rob2)
       rob1 = rob2
       rob2 = temp
       ```
     - Return `rob2`, which represents the maximum amount robbed for the given array.

3. **Calculate Results for Two Cases**:
   - Case 1: Rob houses from the first house to the second-to-last house:
     ```plaintext
     max1 = helper(nums[:-1])
     ```
   - Case 2: Rob houses from the second house to the last house:
     ```plaintext
     max2 = helper(nums[1:])
     ```

4. **Return the Final Result**:
   - Return the maximum of the two cases:
     ```plaintext
     return max(max1, max2)
     ```

### Summary
- **Logic**: By splitting the problem into two non-circular subproblems, we effectively handle the circular constraint while reusing the efficient solution from **House Robber I**.
- **Efficiency**:
  - **Time Complexity**: `O(n)`, as each subproblem is solved in linear time.
  - **Space Complexity**: `O(1)`, due to constant space usage in the helper function.
- **Output**: The function returns the maximum amount that can be robbed without triggering alarms in the circular arrangement of houses.


### Self Notes


```
Iterative approach
"""
   this approach implements a constant space to this dp problem
      we're reusing House Robber 1 solution but with a twist
      we're treating this as two different problems where
         the input is including 0th index but eliminating last value
         the input is eliminating 0th index but including last value
      essentially we need to check two different solutions
         max value including 0th index but eliminating last value
         max value eliminating 0th index but including last value
"""
```
