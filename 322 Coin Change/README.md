# 322. Coin Change

1 possible solution for this problem  

## Method 1

## Problem Intuition
The task is to determine the minimum number of coins needed to make up a given amount using coins of specified denominations. If it is impossible to make up the amount, return `-1`. This problem can be solved using DFS, where we explore all possible combinations of coins and keep track of the minimum coins required.

### Key Insight
1. **DFS for Exploring Options**:
   - At each step, subtract the value of a coin from the amount and recursively calculate the result for the remaining amount.
   - Track the minimum number of coins across all possibilities.
2. **Memoization for Optimization**:
   - Use memoization to store results for already computed amounts, avoiding redundant calculations.

## Approach

### Step-by-Step Solution

1. **Define Recursive Helper Function**:
   - **Input**: Remaining `amount`.
   - **Base Cases**:
     - If `amount == 0`, return `0` (no coins are needed).
     - If `amount < 0`, return `infinity` (indicating this path is invalid).
   - **Memoization Check**:
     - If the result for `amount` is already in the memoization dictionary, return it.
   - **Recursive Exploration**:
     - Initialize `result` to a large value (`infinity`) to track the minimum coins required.
     - Loop through each coin:
       - If the coin value does not exceed the current `amount`, recursively calculate the result for `amount - coin`.
       - Add `1` to the result (indicating this coin is used) and update `result` with the minimum value.
   - **Store in Memoization Dictionary**:
     - Store the result for the current `amount` in the dictionary.
   - Return the computed result.

2. **Initialize Memoization and Call the Helper Function**:
   - Create a memoization dictionary to store results for computed amounts.
   - Call the helper function with the target `amount`.

3. **Handle Edge Cases**:
   - If the result from the helper function is `infinity`, return `-1` (indicating no solution is possible).
   - Otherwise, return the result.

### Example Walkthrough
For `coins = [1, 2, 5]` and `amount = 11`:
- Recursive calls explore combinations such as:
  - Using coin `5`: 5 → 6 → 1 → 0 (4 coins total).
  - Using coin `2`: 2 → 9 → 4 → 2 → 0 (6 coins total).
  - Using coin `1`: Direct subtraction (11 coins total).

### Summary
- **DFS with Memoization Logic**: Explore all possible combinations recursively while storing results for already computed amounts to avoid redundant calculations.
- **Efficiency**:
  - **Time Complexity**: `O(amount * n)`, where `n` is the number of coins. Each amount is computed once, and for each amount, all coins are considered.
  - **Space Complexity**: `O(amount)` due to the recursion stack and memoization dictionary.
- **Output**: The function returns the minimum number of coins needed, or `-1` if it is impossible to form the given amount.


### Self Notes


```
"""
    we can treat this as a dfs problem
        we need to calculate the no. of coins needed for the amount
        we can put a slight twist into the problem
            instead of calculating for each coin & starting from 0
            we can start in desc order from the input amount
            for each coin, subtract the coin's value from needed amount & call recursive function for new wanted value
            get the min value out of all the coins 
    
    create a helper function to implement dfs recursively
        base conditions
            if amount == 0, return 0
        create a variable with max value 
        loop thru all the coins
            check if using the coin won't put value into negative
            if it doesn't, recursively call for the remainder for this coin
                add 1 to indicate this coin has been used
                get the min value of return & above result variable
            after all coins are done, we have the min value in result varaible
        return this value
    
    the return value of initial call for amount will have the no. of coins
"""
```
