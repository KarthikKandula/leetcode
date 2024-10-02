# 206. Reverse Linked List

2 possible solutions for this problem  
- can be done iteratively and recursively

## Method 1 (Iterative Solution)

We can solve this problem by implementing a **basic iterative approach** to reverse a linked list.

#### 1. **Node structure**:
   - Every node in the linked list has two properties:
     - `val`: the current value of the node.
     - `next`: a pointer to the next node in the list.
#### 2. **Reversing the linked list**:
   - The goal is to reverse the direction of each node’s `next` pointer so that it points **backward** instead of forward.
   
   - We’ll use two pointers to help with the reversal:
     - `prev`: points to the **previous node**.
     - `curr`: points to the **current node** being processed.
   
   - **Initial setup**:
     - Set `prev` to `None` because the original head of the list will become the new tail and point to `None`.
     - Set `curr` to the first node (the original head).
#### 3. **Iterative reversal process**:
   - As we loop through each node in the list:
     1. **Save the next node**: Temporarily store the `next` node (`next_node = curr.next`) to prevent losing access to the rest of the list.
     2. **Reverse the link**: Set `curr.next = prev` to reverse the pointer of the current node so it points to the previous node.
     3. **Move pointers forward**: 
        - Set `prev = curr` (current node becomes the previous node for the next iteration).
        - Set `curr = next_node` (move to the next node in the list).
#### 4. **Return the new head**:
   - After the loop ends, `prev` will be pointing to the last node in the original list, which is now the **new head** of the reversed list.
   - Return `prev` as the new head.

This approach efficiently reverses the linked list in a single pass with a time complexity of O(n).

### Self Notes
To achieve this we can use basic implementation of linked list in a iterative way.
every node has two values, val -- indicates current value & next -- links to next value. The task is to reverse every single node so that the next value points backward. to do this we'll loop thru each node taking two pointers -- prev -- points to the previous node & curr -- points to the current node. as we're looping thru the nodes, we want to reverse the link (set next to previous node) & setup prev & curr in such a way that they're useful for the next iteration. initially we'll set prev to none & curr to the first node, as we're looping thru the nodes, we'll perform the decided upon operations & return the prev value at the end. since in every loop the current node will always become prev & by the end of the loops, prev would be the last node which will be the new head

```
"""
    Iterative solution

    every node has two values
        val -- indicates current value
        next -- links to next value

    we take two pointers
        prev -- points to the previous node
        curr -- points to the current node

    loop as long as the curr node is valid
        assign next value to a temp node
        assign previous value to the next value in current node -- essentially reversing the chain
        assign current node to prev node -- helpful for ops in next iteration
        assign temp node (next node value) to curr node -- helpful for ops in next iteration

        in this loop we're 
            reversing the chain
            and updating prev & curr pointers so they're helpful for the next loop
"""
```


## Method 2 (Recursive Solution)

We can solve this problem by implementing a **recursive approach** to reverse a linked list.

#### 1. **Node structure**:
   - Every node in the linked list has two properties:
     - `val`: the current value of the node.
     - `next`: a pointer to the next node in the list.
#### 2. **Recursive approach**:
   - The key to any recursive solution is having:
     1. A **base condition**: which acts as a stopping point for recursive calls.
     2. A **recursive function call**: which keeps the function repeating for each node.
#### 3. **Reversing the linked list recursively**:
   - The task is to reverse each node so that the `next` pointer points **backward**.
   
   - We’ll use two pointers:
     - `prev`: points to the **previous node**.
     - `curr`: points to the **current node** being processed.
#### 4. **Base condition**:
   - The base condition is when the current node (`curr`) becomes `None`, which means we’ve reached the end of the list. At this point, we stop the recursive calls and return the `prev` node, which will be the **new head** of the reversed list.
#### 5. **Recursive function call**:
   - For each node:
     1. **Save the next node**: Temporarily store `curr.next` to ensure we don’t lose access to the rest of the list.
     2. **Reverse the link**: Set `curr.next = prev` to point the current node to the previous node, reversing the link.
     3. **Move forward**: Make a recursive call to process the next node, passing the current node (`curr`) as the new `prev` and `next_node` as the new `curr`.
#### 6. **Initial setup**:
   - Set `prev` to `None` (since the original head will become the new tail) and `curr` to the first node.
   - Begin the recursion, performing the above operations at each step.
#### 7. **Return the new head**:
   - Once the recursion unwinds, the `prev` pointer will be at the last node of the original list, which becomes the **new head** of the reversed list.
   - Return `prev` as the result.

This approach recursively reverses the linked list, with each node processed in a manner similar to an iterative approach, but with the help of function calls instead of loops.

### Self Notes
To achieve this we can use basic implementation of linked list in a recursive way.
The main point to any recursive operation is a base condition & recursive function call. the base condition acts as a means to stop the recursive calls & the function call serves as a way to call the function repeatedly. every node has two values, val -- indicates current value & next -- links to next value. The task is to reverse every single node so that the next value points backward. to do this we'll go thru each node taking two pointers -- prev -- points to the previous node & curr -- points to the current node. as we're processing thru the nodes, we want to reverse the link (set next to previous node) & setup prev & curr in such a way that they're useful for the next recursive function. initially we'll set prev to none & curr to the first node, as we're making function calls reversing thru the nodes, we'll perform the decided upon operations & return the prev value at the end. since in every loop the current node will always become prev & by the end of the loops, prev would be the last node which will be the new head. The base function here is when curr node become none, we want to end the function calls

```
"""
    Recursive solution
        the solution is very similar to iterative solution but just with recursive characteristics

    every node has two values
        val -- indicates current value
        next -- links to next value

    in the recursive function we take two pointers
        prev -- points to the previous node
        curr -- points to the current node

    in any function call, perform the following
        base condition -- check if curr node is none - if it is, return prev node
        assign next value (from curr node) to a temp node
        assign prev value to the next value in curr node -- essentially reversing the chain
        we're performing the below two functions as part of the recursive function call
            assign curr node to prev node -- helpful for ops in next iteration
            assign temp node (next node value) to curr node -- helpful for ops in next iteration

        in this loop we're 
            reversing the chain
            updating prev & curr pointers so they're helpful for the next loop
"""
```
