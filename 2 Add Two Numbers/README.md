# 2. Add Two Numbers

1 possible solution for this problem  

## Method 1

We solve this problem using basic linked list traversal and arithmetic. The given linked lists represent numbers in reverse order, which simplifies addition since we naturally add numbers from the least significant digit to the most significant digit.

#### 1. **Node structure**:
   - Each node in the linked list has:
     - `val`: the digit value of the node.
     - `next`: a pointer to the next node.

#### 2. **Approach**:

1. **Initialize pointers and carry**:
   - Use pointers to traverse through both input linked lists (`l1` and `l2`).
   - Keep track of the carry, initialized to `0`, which is used when the sum of two digits exceeds `9`.

2. **Traverse and sum the nodes**:
   - Loop through the linked lists as long as either `l1` or `l2` has values, or if there is a carry.
   - At each iteration:
     - Get the values from the current nodes of `l1` and `l2` (use `0` if the node is `None`).
     - Calculate the sum of the values plus the carry.
     - Determine the new carry (`sum // 10`) and the digit to insert into the new node (`sum % 10`).
     - Create a new node with the digit value and attach it to the result list.

3. **Update pointers**:
   - Move the pointers for `l1` and `l2` to the next nodes.
   - Update the pointer for the result list to point to the new node.

4. **Return the result**:
   - The result linked list starts from the dummy node’s `next` pointer since the dummy node itself is just a placeholder.

#### 3. **Time and Space Complexity**:
   - The approach runs in **O(max(m, n))** time, where `m` and `n` are the lengths of the input linked lists.
   - The space complexity is **O(max(m, n))** for storing the new linked list.

### Self Notes
To achieve this we can use basic linked list traversal along with a basic math to solve the problem. if we remember how to add numbers in match, we add them in reverse order anyways, here giving the linked list in reverse order is actually helping us.
every node has two values, val -- indicates current value & next -- links to next value. we're asked to sum the numbers & return result in a new linked list. the thing we need to manage here is the carry's, since that's the basic in adding two numbers, we need to keep track of carrys. so the program goes like, loop thru the input lists while any one of them is valid & if carry has a value, get values at that location, add them with carry. get the carry for the sum (using // - gets multiple) & the value to insert into the node (using % - gets the remainder), insert this value into a new node & update all pointers for next iteration. do it until the end & we have the result linked list.

```
"""
   use basic linked list traversal along with basic math to solve the problem

   if we remember how to add numbers in match, we add them in reverse order anyways
      here giving the linked list in reverse order is actually helping us

   create a variable to hold carry at each location - initially set to 0

   loop thru the list while any of the current list has a number or carry is not 0
      get the value at that location from each list
      add values at that location from each list & carry
      get the carry value from sum -- get multiple using //
      get the remainder from sum -- to insert into next node -- using %

      insert remainder into a newly created node & assign it to curr.next

      update all pointer for next iteration

   return dummy's next at the end
"""
```