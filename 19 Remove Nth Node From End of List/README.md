# 19. Remove Nth Node From End of List

2 possible solutions for this problem  

update writeup for my solution

## Method 1

We can solve this problem using a **two-pointer approach** to efficiently remove the n-th node from the end of a linked list.

#### 1. **Node structure**:
   - Every node in a linked list has two properties:
     - `val`: the current value of the node.
     - `next`: a pointer to the next node in the list.
#### 2. **Using two pointers (left and right)**:
   - We will use two pointers, `left` and `right`, to traverse the list and locate the node that needs to be removed:
     1. **Set the `left` pointer** to the **head** of the linked list.
     2. **Move the `right` pointer** `n` steps forward from the head, where `n` is the position of the node to remove from the end.
#### 3. **Handle edge case**:
   - After moving the `right` pointer `n` steps:
     - If the `right` pointer reaches `None`, this means we need to **remove the first node** (i.e., the head of the list). In this case, simply return `head.next` as the new head of the list.
#### 4. **Move both pointers**:
   - If the list is longer than `n` nodes:
     - Move both `left` and `right` pointers **one step at a time** until `right` reaches the end of the list (`None`).
     - At this point, the `left` pointer will be just before the node that needs to be removed.
#### 5. **Remove the target node**:
   - To remove the target node:
     - Set `left.next = left.next.next`, which bypasses the node to be removed and links the node before it to the node after it.
#### 6. **Return the updated list**:
   - Return the `head` of the modified list after the removal is complete.

This approach allows the removal of the n-th node from the end in **O(n)** time, where `n` is the length of the linked list, using constant space **O(1)**.

### Self Notes
To achieve this we can use basic implementation of linked list with two pointers - left & right. first we assign left to head & move right n number of places as in input. after this we check if n is empty since that means we have to remove first node, remove it & return the rest -- this is an edge case. after that we move left & right one position each until right reaches the end. At that point left points to the node that is just before the one that should be removed. we remove the link using left.next = left.next.next, after that we return head

```
"""
   Neetcode influenced own solution

   the objective is to remove nth node from the last
      the way we can go to this location at once is if we use two pointers
         left - starts at head
         right - initially starts n places from left
               at this point we handle a edge case where the first node has to be removed
      after that we advance left & right equally until right reaches end
   
   at this point left points to the before node of the one that has to be removed
      kill the link to the node that has to be removed & create link to the node after that
   
   return head at the end
"""
```

## Method 2 (My solution)

We can solve this problem by using a **hashmap** to store node positions, followed by a traversal to remove the target node.

#### 1. **Node structure**:
   - Every node in a linked list has two properties:
     - `val`: the current value of the node.
     - `next`: a pointer to the next node in the list.
#### 2. **Step-by-step approach**:
1. **First traversal - Store values in a hashmap**:
   - Traverse the linked list once and store each node's value along with its position in a hashmap.
     - For example: `{position: node}`, where `position` is the index of the node in the list.
2. **Calculate target node**:
   - Using the total length of the linked list and the value `n` (position of the node from the end), calculate the position of the node that needs to be removed.
     - The target position can be derived as `length - n`.
3. **Second traversal - Remove target node**:
   - Traverse the linked list again, and this time, look for the target node at the calculated position.
     - Once the target node is found, modify the previous node's `next` pointer to skip the target node. This is done by setting `prev.next = prev.next.next`, effectively "removing" the target node from the list.
4. **Return updated list**:
   - After removing the target node, return the `head` of the updated linked list.
#### 3. **Edge Case**:
   - If the target node to remove is the first node (head), simply return `head.next` to update the head of the list.
   
This method works in **O(n)** time, where `n` is the length of the list, but requires additional space of **O(n)** to store node positions in the hashmap.

### Self Notes
To achieve this first we go thru the linked list & insert the values along with their positions in a hashmap. now calculate the target node that has to be removed. Again go thru the linked list now looking for the target value. once at the target value, replace prev next to the next's value essentially killing the link to the target value. after that we return head. 

