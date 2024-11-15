# 70. Climbing Stairs

1 possible solution for this problem  

## Method 1 (Recursive approach)

## Problem Intuition
The task is to find the number of distinct ways to climb a staircase of `n` steps, where you can climb either 1 or 2 steps at a time. This can be solved using recursion, where each step depends on the number of ways to reach the previous step and the step before that. However, a purely recursive solution can have exponential complexity due to repeated calculations. Using **memoization**, we store and reuse results of previous computations to optimize the solution.

## Approach

### Key Idea
1. **Use Recursion with Memoization**:
   - Create an array `memo` to store results for each step. This avoids redundant calculations and reduces the time complexity.
   - For each step, check if the result is already calculated in `memo`. If so, return the value directly.

### Step-by-Step Solution

1. **Initialize Memoization Array**:
   - Create an array `memo` of size `n+1`, initialized to `-1`. This represents that no steps have been calculated yet.

2. **Define Recursive Function**:
   - **Base Cases**:
     - If `n == 0`, return `1` (only one way to stay at the ground).
     - If `n == 1`, return `1` (only one way to climb one step).
   - **Check Memoized Value**:
     - Before making recursive calls, check if `memo[n]` is not `-1`. If it’s already calculated, return `memo[n]`.
   - **Calculate Ways for Current Step**:
     - Otherwise, compute `memo[n]` as the sum of the ways to climb `n-1` steps and `n-2` steps:
       ```plaintext
       memo[n] = climb(n-1) + climb(n-2)
       ```
   - Return `memo[n]`.

3. **Call Recursive Function**:
   - Start the recursive function with the input `n` to calculate the number of ways to climb `n` steps.

4. **Return Result**:
   - The result for `n` steps will be stored in `memo[n]`.

### Summary
- **Memoization Logic**: The `memo` array stores results for previously calculated steps, significantly reducing the number of recursive calls.
- **Efficiency**: Time complexity is `O(n)` as each step is calculated only once, and space complexity is `O(n)` due to the recursion stack and `memo` array.
- **Output**: Return `memo[n]`, representing the number of ways to climb `n` steps.

### Self Notes

```
Memoized recursive approach
"""
   this implements the same regular recursive approach but elimates a layer of recursive function calls

   take an array initialized to -1 for the length of input n
      -1 indicates this value isn't yet calculated
   
   now in a function call before making recursive calls
      check if the array has been initialized at this index
      if it is, return the value -- reducing the amount of function calls by reusing them effectively
"""

Regular recursive approach
"""
   we can use regular recursion to solve the problem
   
   create a helper function to implement recursively
      input is the stair num
      check base conditions
         if input equal to n 
            target is reached
            return 1 to signify a way has been found
         if input is greater than n
            target is overshot
            return 0 to signify this is not a way
      
      recursively call stair + 1 and stair + 2
         return their added value
   
   return the return value of first function call for index 0
"""
```
