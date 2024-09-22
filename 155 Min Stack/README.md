# 155. Min Stack

1 possible solution for this problem  

## Method 1

We can implement a **Minimum Stack** using two stacks:

1. **Use two stacks**:
   - One stack (`stack`) to hold all the values.
   - Another stack (`minStack`) to track the minimum values as they appear.
2. **Push operation**:
   - Push the value onto the `stack`.
   - Push the value onto the `minStack` if it is less than or equal to the current minimum, or if `minStack` is empty.
3. **Pop operation**:
   - Pop the value from the `stack`.
   - If the popped value matches the top value of the `minStack`, pop it from `minStack` as well.
4. **Get minimum operation**:
   - The top of the `minStack` always holds the minimum value, so retrieving the minimum is simply returning the top of the `minStack`.

By maintaining two stacks, we efficiently handle all operations while keeping track of the minimum value in constant time.

### Self Notes
the problem statement is to implement a minimum stack. an extra operation is to create a function to retrieve the minimum element upon request. For this we create two stacks, one to hold the stack values & the other one to hold minimum values in the stack as they appear. On every push operation, we push into the actual stack & push into minStack based upon the value. Same with pop, if the popped value from actual stack is the top value in minStack we pop it out too. Do this for as many operations as requested. 

