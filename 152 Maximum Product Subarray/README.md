# 152. Maximum Product Subarray

1 possible solution for this problem  

## Method 1

## Problem Intuition
The task is to find the contiguous subarray within an array (containing at least one number) that has the largest product. The challenge lies in handling negative numbers, as they can either increase or decrease the product depending on the context. To address this, we track both the maximum and minimum product at each step, as a negative number can turn the minimum product into a maximum when multiplied.

### Key Insight
1. **Track Maximum and Minimum Products**:
   - Maintain two variables:
     - `curMax`: Tracks the maximum product up to the current index.
     - `curMin`: Tracks the minimum product up to the current index.
   - Update these values as you iterate through the array.

2. **Handle Zeroes**:
   - If the current number is `0`, reset `curMax` and `curMin` to `1` to effectively restart the product calculation for subsequent elements.

## Approach

### Step-by-Step Solution

1. **Initialize Variables**:
   - Set `result` to the maximum value in the input array to handle edge cases where all numbers are negative or contain zeroes.
   - Initialize `curMax` and `curMin` to `1`.

2. **Iterate Through the Array**:
   - For each number in the array:
     - If the number is `0`:
       - Reset `curMax` and `curMin` to `1`, as the product is interrupted.
     - Store `curMax` in a temporary variable to avoid using the updated `curMax` value when calculating `curMin`.
     - Update `curMax` as the maximum of:
       - The current number.
       - The current number multiplied by the previous `curMax`.
       - The current number multiplied by the previous `curMin`.
     - Update `curMin` as the minimum of the same three values.
     - Update `result` as the maximum of `result` and `curMax`.

3. **Return the Result**:
   - After processing all numbers, `result` contains the maximum product of any contiguous subarray.

### Example Walkthrough
For `nums = [2, 3, -2, 4]`:
- At index `0`: `curMax = 2`, `curMin = 2`, `result = 2`.
- At index `1`: `curMax = 6`, `curMin = 3`, `result = 6`.
- At index `2`: `curMax = -2`, `curMin = -12`, `result = 6`.
- At index `3`: `curMax = 4`, `curMin = -48`, `result = 6`.

For `nums = [-2, 3, -4]`:
- At index `0`: `curMax = -2`, `curMin = -2`, `result = -2`.
- At index `1`: `curMax = 3`, `curMin = -6`, `result = 3`.
- At index `2`: `curMax = 24`, `curMin = -12`, `result = 24`.

### Summary
- **Dynamic Programming Logic**:
  - Track both `curMax` and `curMin` to handle the impact of negative numbers.
  - Reset on encountering zero to effectively restart subarray calculations.
- **Efficiency**:
  - **Time Complexity**: `O(n)`, as we traverse the array once.
  - **Space Complexity**: `O(1)`, as only a few variables are used.
- **Output**: The function returns the maximum product of any contiguous subarray.


### Self Notes


```
"""
   this is a traditional dp problem
      a major issue appears with -ve numbers since it keeps fluctuating b/w +ve & -ve with each multiplication
      to get around this issue, we keep track of max product until now & min product until now
      keep updating this value as we keep moving along in the array
      so essentially, we're keeping track of both min & max values since with -ve values they can swing in any direction
   
   create a result variable, assign max value from the input
   create two variables, assign both to 0
      curMax -- tracks the max value 
      curMin -- track the min value 

   loop thru the input
      if any number is 0, assign curMax, curMin to 1
         making them neutral & cutting off product values from before
      assign curMax to temp variable 
         to use in calculating curMin so as to not use newly calculated curMax
      cacluate new curMax for this number
         take the max of current number multiplies by curMax, curMin & itself alone
      cacluate new curMin for this number
         take the min of current number multiplies by curMax, curMin & itself alone
      get max value for result variable
   
   in the end, return result variable
"""
```
