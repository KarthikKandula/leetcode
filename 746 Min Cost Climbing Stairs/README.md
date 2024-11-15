# 746. Min Cost Climbing Stairs

1 possible solution for this problem  

## Method 1 (Recursive approach)

## Problem Intuition
The goal is to minimize the total cost of climbing a staircase, where each step has a given cost. You can start from either step 0 or step 1, and at each step, you can climb one or two steps. This problem can be solved as a dynamic programming problem, where we calculate the minimum cost to reach the top from each step using recursion with memoization.

## Approach

### Key Idea
1. **Dynamic Programming with Memoization**:
   - Use a `cache` array to store the minimum cost to reach the top from each step, avoiding redundant calculations.
   - At each step, calculate the cost as the sum of the current step’s cost and the minimum cost of the next one or two steps.

### Step-by-Step Solution

1. **Initialize Memoization Array**:
   - Create a `cache` array of size equal to the length of `cost`, initialized with `-1` to indicate uncomputed values.

2. **Define Recursive Helper Function**:
   - **Input**: Current step index `i`.
   - **Base Case**:
     - If `i >= len(cost)`, return `0`, as no cost is needed beyond the last step.
   - **Check Cached Value**:
     - If `cache[i]` is not `-1`, return `cache[i]`, indicating this step’s result has already been computed.
   - **Calculate and Store Result**:
     - Compute `cache[i]` as the cost of the current step plus the minimum cost of taking one or two steps forward:
       ```plaintext
       cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
       ```
   - Return `cache[i]`.

3. **Call the Recursive Function**:
   - Since the climb can start from either step `0` or step `1`, compute the result as:
     ```plaintext
     min(dfs(0), dfs(1))
     ```

4. **Return the Final Result**:
   - The result is the minimum cost to reach the top starting from either step 0 or step 1.

### Summary
- **Memoization Logic**: The `cache` array stores the minimum cost to reach the top from each step, significantly reducing redundant calculations.
- **Efficiency**:
  - **Time Complexity**: `O(n)`, as each step is processed only once.
  - **Space Complexity**: `O(n)` due to the recursion stack and the `cache` array.
- **Output**: Return the minimum cost to climb to the top of the stairs.


### Self Notes

```
"""
   Recursion w/ memoization

   we can treat this as a dynamic programming problem with memoization
      each step has a cost, and we want to reach the top with the minimum total cost
      at each step, we decide whether to move one or two steps forward, accumulating the minimum cost

   create a cache array to store intermediate results
      initialize the cache with -1 values, indicating uncomputed states
      cache stores the minimum cost to reach the top from each step, reducing redundant calculations

   define a recursive helper function `dfs` to calculate the minimum cost to reach the top
      input is the current step index (i)

      check if the step index has reached or exceeded the end of the cost array
      if it has, return 0 as no cost is needed beyond the last step
      check if the cache already has a computed value for this step
      if it does, return that cached value to avoid recalculating

      calculate and store the result in cache
      the minimum cost at step i is the cost of the current step plus the minimum of the costs of the next two steps

   call the helper function starting from the first two steps
      take the minimum of starting from step 0 and step 1 as the final result
      this gives the minimum cost to reach the top of the stairs
"""
```
