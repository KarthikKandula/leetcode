# 141. Linked List Cycle

1 possible solution for this problem  

## Method 1

We solve this problem using **Floyd's Tortoise and Hare** algorithm, which is an efficient way to detect cycles in a linked list.

#### 1. **Algorithm Overview**:
   - The algorithm uses two pointers:
     - **Slow Pointer** (`slow`): Moves 1 position in each iteration.
     - **Fast Pointer** (`fast`): Moves 2 positions in each iteration.
   - If there is a cycle, these two pointers will eventually meet. If there is no cycle, the `fast` pointer will reach the end of the list (`None`).

#### 2. **Steps**:

1. **Initialize the pointers**:
   - Set both the `slow` and `fast` pointers to the head of the linked list.

2. **Traverse the linked list**:
   - Move the `slow` pointer by 1 step and the `fast` pointer by 2 steps in each iteration.
   - Check if the `slow` and `fast` pointers meet:
     - If they do, a cycle is detected.
     - If the `fast` pointer reaches the end (`None`), then there is no cycle.

3. **Time Complexity**:
   - The algorithm runs in **O(n)** time, where `n` is the number of nodes in the linked list.

4. **Space Complexity**:
   - The algorithm uses **O(1)** space since only two pointers are used.

By implementing the above approach, we efficiently determine if a linked list contains a cycle.

### Self Notes
To achieve this we can use Floyd's Tortoise & Hare algorithm to solve the problem. The algorithm uses two pointers slow & fast, slow -- moves 1 position with each iteration, fast - moves 2 positions with each iteration. the algorithm says these two pointers will meet eventually within n iterations if there is a cycle in the list. time complexity is O(n).

```
"""
   use Floyd's Tortoise & Hare algorithm to solve the problem
      this uses two pointers - slow & fast
         slow -- moves 1 position with each iteration
         fast -- moves 2 positions with each iteration
      the algorithm says these two pointers will meet eventually if there is a cycle within n iterations
         time complexity is O(n)
   
   take two pointers -- slow & fast

   loop while fast & fast.next is valid
      move slow by 1 position
      move fast by 2 positions
      if slow & fast are equal return true

   in the end return false -- only hits if return is not hit within loop
"""
```