# 84. Largest Rectangle in Histogram

1 possible solution for this problem  

## Method 1

We can solve this problem using a **stack** with a strategy to store index-height pairs and calculate the largest rectangle efficiently.

1. **Stack for pairs (index, height)**:
   - The stack stores pairs of `(index, height)` as we loop through the input heights.
   - For each height, before pushing it onto the stack, check if there are any heights in the stack that are **greater than** the current height. If so, these heights can't extend forward, so we can pop them out.
2. **Calculate max area while popping**:
   - As we pop out the heights, calculate the max area for each popped height using the formula:  
     `max area = height * (current index - popped index)`
   - This formula works because the popped height can extend back to its original index but can't extend forward beyond the current index. 
3. **Extend current height backward**:
   - When popping, we can extend the current height backward using the popped index. So, when inserting the current height into the stack, use the index of the last popped height (since it can extend backward to that index).
4. **After the loop**:
   - Once the input is fully traversed, there may still be elements in the stack. For these, calculate the max area using the formula:  
     `max area = height * (length of input - index)`
   - This accounts for heights that extend to the end of the histogram.
5. **Final result**:
   - By the end of the loop and post-processing the stack, the maximum area will be stored in the `maxArea` variable.

This approach ensures that all possible rectangles are efficiently calculated, and we always maintain the largest possible area.

### Self Notes
We can use stack to solve the problem, trick is to save to stack in pairs - (index, height). while looping thru the input, before pushing current height to stack, check if there are any in the stack that are higher than current height, if there are it means they can't be extended forward, so we can pop them out. but at the same time the current height can be extended backward, so while popping it out, we get the index & height, calculate max area for the popped out variable & replace the max variable. max area is calculated using formula - (height * (current index - index)). also while inserting current value, use index of any popped out value (since can be extended backwards). After input is traversed, there is a possiblity for some elements to stay in stack, loop thru the stack again to get any max area using formula (height * (length of input - index)). by the end max area is in the maxArea variable

```
"""
   use stack to solve the problem
      trick is to store values in pairs in stack - (index, height)

   loop thru the input
      check if there are any values in the stack that are greater than current height
         if there are, pop them all out since they can't be extended forward to current height, they have been broken
               get the max area of the popped value & replace if max
               since the popped value is greater than current, it means current height can be extended back, so we take the index of that variable 
      append current height to stack with
         our own index if there are no values higher in stack
         if we popped any values out, we use that index value, there is a variable for this

   after looping thru all the values, there might still be values in the stack
      to find if there is a possibility of max area in those, 
      loop thru the stack 
         find max area for each value in stack - use formula (height * (length of input - index))
         replace if max
   
   loop to the end & maxArea variable will have max value
"""
```
