# 239. Sliding Window Maximum

1 possible solution for this problem

## Method 1

We can solve this using the **sliding window** approach and a **deque** to keep track of the maximum values efficiently.

1. **Use a deque for indices**: 
   - The deque will store the indices of the elements in the `nums` array, and it will maintain elements in descending order, with the largest element's index always at the front.
   - This ensures the leftmost value in the deque is always the maximum in the current window.
2. **Loop through the `nums` array**:
   - As you move the `right` pointer (sliding the window), for each index, remove indices from the deque that point to values smaller than the current element. This keeps the deque ordered with the largest values on the left.
   - After insertion, if the index at the left of the deque is outside the current window (i.e., it is less than the current `left` pointer), remove it from the deque.
3. **Check when to add to output**:
   - Once the window has grown to the required size (i.e., `right + 1 >= k`), insert the element at the front of the deque (which represents the largest value in the window) into the output array.
   - Then, increment the `left` pointer to slide the window forward.
4. **Continue until the end**: Repeat this process until the `right` pointer reaches the end of the `nums` array. The output array will then contain the maximum values for each window.

This method ensures we maintain the maximum efficiently in each sliding window, with all the required values stored in the output array.

### Self Notes
To achieve this we can use the sliding window method approach. And also use a deque to keep track of values in the input nums array, one thing about deque is that values are ordered in descending order. We need to insert & remove the values into the deque so that the highest value is always towards the left of the deque. Also another thing to note is that we use indexes to insert into the deque rather than the actual values themselves.  
While looping thru the input nums, (using the right pointer) insert every index into the deque, also check if there are any values less than the current value, if there are, pop all those values. After inserting, check if the left most value is greater than the current left pointer - to make sure there are no values in the queue that are outside the current window. Finally, check if the current window is in a position where we can start inserting values into the output array. basically checking if the right pointer has passed thru enough values that it is greater than or equal to k (r+1 >= k), if it is insert left most value from deque into output, since that's where the highest number is stored & increment the left pointer to keep the window moving. Loop thru the end & all required values are in the output array.

```
"""
   Use sliding window approach to solve the problem
      Use deque to keep track of the highest number from a window
         deque - always orders the values by descending order
      Another important detail is to insert indexes into the deque rather than the actual values

   loop thru input array - using right pointer
      insert current right pointer index into deque
      before inserting check if there are any values less than the current value
         if there are pop them all out - in a loop

      after inserting current value
      check if the left most value in greater than left pointer - to adjust values in deque according to the current window
         if there are, pop those values out

      check if the right pointer has come to a position where we can start inserting into the output array
         if it is, insert the left most deque value into the output, since it's the highest

   loop thru the end of the string
      since we're updating output throughout the loop, return output as answer
"""
```
