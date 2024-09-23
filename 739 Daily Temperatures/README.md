# 739. Daily Temperatures

1 possible solution for this problem  

## Method 1

We can solve this problem using a **monotonic stack**. A monotonic stack maintains elements in decreasing order, and the goal is to track which values appear before the current one and update the result array accordingly.

1. **Monotonic stack**:
   - The stack will store values as we traverse through the input array. We make the stack monotonic by ensuring that values are always in decreasing order.
2. **Result array**:
   - Another array will be used to store the final output, where each index will be updated based on the value comparisons.
3. **Loop through the input array**:
   - For each element, check if it is greater than the elements in the stack. If it is, update the corresponding index in the result array with the difference between the current index and the index of the popped element.
   - Continue popping elements from the stack as long as they are less than the current value.
   - After processing, append the current value (or its index) to the stack.
4. **Final result**:
   - Once the entire input array is processed, the result array will contain the desired output.

This approach efficiently solves the problem by ensuring values are maintained in decreasing order in the stack and updating the result array in constant time for each element comparison.

### Self Notes
We can use stack (monotonic stack) to solve the problem in an effective manner, It's not a prefix implementation in python, we make it monotonic in our code - it means values are always in decreasing order. the entire problem depends on knowing what values appear before it & updating the values based on index in the result array. To do this we'll take two arrays (stacks), one for storing values as we traverse thru them (this is the monotonic stack), other for storing the output result. loop thru the input array, for every value that is less than the current value, update it's corresponding index with the difference in indexes, after there are no values less than the current, append current value to stack. Once entire input is traversed, output is in result array.

```
"""
   Use stack (monotonic stack) to solve the problem
      It's not a prefix implementation in python, we make it monotonic in our code - it means values are always in decreasing order

   Create two arrays (stacks) 
      one for storing the values as we traverse thru them
      other for storing the output result

   loop thru the input temperatures
      check if there are any values in the stack that are less than current temperature (in a while loop)
         if there are, we have the answer for that index
               pop the value, update the index of popped value - subtract it with the current index
         do it until there are no values less than current in the stack
      if there are no values less than current, append current value to the stack
         append in the format (temperature, index) - use to subtract index value with current index while updating result array
   once traversed thru all the input, output is in result array
"""
```
