# 143. Reorder List

1 possible solution for this problem  

## Method 1

We can solve this problem using an **in-place** approach to modify the linked list without creating a new one.

#### 1. **Node structure**:
   - Every node in a linked list has two properties:
     - `val`: the current value of the node.
     - `next`: a pointer to the next node in the list.
#### 2. **In-place modification**:
   - Since we are asked to reorder the list **in-place**, we cannot create a new list. Instead, we will:
     1. **Split the list into two halves**.
     2. **Reverse the second half**.
     3. **Merge the two halves** back together by alternating nodes from each half.
#### 3. **Steps**:
1. **Find the middle of the list**:
   - Use the **slow and fast pointer technique**. Initialize both pointers at the head:
     - `slow` moves one step at a time.
     - `fast` moves two steps at a time.
   - By the time `fast` reaches the end of the list, `slow` will be at the middle.
2. **Reverse the second half**:
   - Once the list is split into two halves, **reverse the second half**. This will allow us to merge the two halves easily.
   - To reverse the second half, use a standard linked list reversal technique (use two pointers: `prev` and `curr`).
3. **Merge the two halves**:
   - Now, interleave the nodes from the first half and the reversed second half:
     - Use temporary pointers to manipulate the `next` pointers and combine nodes from both halves.
     - Start with a node from the first half, then alternate with a node from the reversed second half.
#### 4. **In-place update**:
   - The key part of the problem is to **modify the original list** using only temp pointers and without extra memory for a new list.
   - As you merge the nodes, update the `next` pointers of the current nodes in-place to form the new reordered list.
#### 5. **Returning the updated list**:
   - After merging the nodes, the list is now reordered in place, so return the head of the modified list.

This approach allows for efficient reordering of the linked list in **O(n)** time and **O(1)** space, where `n` is the number of nodes in the list.

### Self Notes
To achieve this we can use basic implementation of linked list but use a couple more steps.
every node has two values, val -- indicates current value & next -- links to next value. since we're asked to update the list in place, we have to do just use temp nodes & update the current list, can't create a new list. based on how the problem is worded, we can solve this if we can divide the list into two halfs, first subarray & second subarray. Then we reverse the second subarray since that makes it easier for us to know the next nodes in the second array. after reversing it, it's just doing plain manipulation using temp nodes by updating in place. 

```
"""
   we can use basic linked list manipulation techniques to solve the problem
      if we can find the second half of the list & manage to reverse it
      at the end it's just joining both the lists

   the problem can be divided into two parts
      need to divide the list into two subarrays
         first - has the first half of the list (bigger if odd)
         second - has the second half of the list

   now we reverse second subarray of the list

   after reversing, manipulate the nodes in such a way that they're placed in the asked format
      might have to use multiple temporary nodes
"""
```