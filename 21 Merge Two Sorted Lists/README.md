# 21. Merge Two Sorted Lists

2 possible solutions for this problem  
- can be done iteratively and recursively

## Method 1 (Iterative Solution)

We can solve this problem by implementing an **iterative approach** to merge two sorted linked lists into one sorted list.

#### 1. **Node structure**:
   - Every node in a linked list has two properties:
     - `val`: the current value of the node.
     - `next`: a pointer to the next node in the list.
#### 2. **Using a dummy node**:
   - To simplify the process of merging, we can create a **dummy node**. This will act as a placeholder at the start of the new merged list.
   - We will also use a `tail` pointer, which will point to the **last node** of the merged list as we build it.
#### 3. **Merging the lists**:
   - Set the `tail` pointer to point to the dummy node.
   - Loop through both linked lists (`list1` and `list2`):
     1. Compare the values of the current nodes from both lists.
     2. Attach the node with the smaller value to the `tail` (i.e., the merged list).
     3. Move the pointer of the corresponding list (either `list1` or `list2`) to its `next` node.
     4. Move the `tail` pointer to the newly attached node.
#### 4. **Handling remaining elements**:
   - After the loop, one of the lists may still have remaining elements.
   - If either list still contains nodes, simply attach the rest of that list to the `tail`, as it is already sorted.
#### 5. **Returning the new merged list**:
   - The merged list starts right after the dummy node, so return `dummy.next` as the head of the new list.
#### 6. **Initial setup**:
   - Initialize `dummy` as a new node with an arbitrary value.
   - Initialize `tail` to point to `dummy`.

This approach efficiently merges two sorted lists in a time complexity of O(n + m), where `n` and `m` are the lengths of the two lists.

### Self Notes
To achieve this we can use basic implementation of linked list in a iterative way.
every node has two values, val -- indicates current value & next -- links to next value. since we're creating a new list, it's better to create a dummy node & take a temp variable tail (on which all the operations happen). now loop thru both lists & attach lower value to tail & update the corresponding lists value to next. once both lists have been traversed, check if there's anything left from either of the lists, if there is attach the entire remianing list to tail. in the end return dummy's next value since that's where the entire new list starts

```
"""
  the solution uses classic linked list traversal technique to sort the two lists
      the additional part here being creating a dummy node to get things started. 

  create a temp node called tail that will be the running node where things will be added to. 

  loop while both lists are valid
      check for the lowest value and add it to the list first
          adding to the list means, adding it to tail
          after adding make sure to update the respective list's node to the next value
      in every loop, make sure to update tail to become the last node -- useful for next iterations
  
  it is possible some lists are longer than others so the previous loop ends without going thru everything
      check if anything is left in the lists
          if there is, assign remaining of the list to tail
  
  in the end return dummy's next value -- that's where the new list starts
"""
```


## Method 2 (Recursive Solution)

need to learn recursive solution

### Self Notes
To achieve this we can use basic implementation of linked list in a recursive way.
The main point to any recursive operation is a base condition & recursive function call. the base condition acts as a means to stop the recursive calls & the function call serves as a way to call the function repeatedly. every node has two values, val -- indicates current value & next -- links to next value. The task is to reverse every single node so that the next value points backward. to do this we'll go thru each node taking two pointers -- prev -- points to the previous node & curr -- points to the current node. as we're processing thru the nodes, we want to reverse the link (set next to previous node) & setup prev & curr in such a way that they're useful for the next recursive function. initially we'll set prev to none & curr to the first node, as we're making function calls reversing thru the nodes, we'll perform the decided upon operations & return the prev value at the end. since in every loop the current node will always become prev & by the end of the loops, prev would be the last node which will be the new head. The base function here is when curr node become none, we want to end the function calls

```
"""
  
"""
```
