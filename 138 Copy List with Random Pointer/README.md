# 138. Copy List with Random Pointer

1 possible solution for this problem  

## Method 1

We can solve this problem using basic linked list traversal and a hashmap to store node copies. The approach involves two passes through the list.

#### 1. **Node structure**:
   - Every node in the linked list has:
     - `val`: the current value of the node.
     - `next`: a pointer to the next node.
     - `random`: a pointer to a random node within the list.

#### 2. **Approach**:

1. **First Pass - Create copy nodes**:
   - Traverse the original linked list and create a copy node for each node.
   - Store each original node and its corresponding copy node in a hashmap in the format: `{original_node: copy_node}`.
   - This allows us to reference and access the copied nodes quickly in the next step.

2. **Second Pass - Set up `next` and `random` pointers**:
   - Traverse the linked list again, using the hashmap to get the copy node for each original node.
   - Set the `next` and `random` pointers for each copy node using the values from the original node:
     - `copy_node.next = hashmap[original_node.next]`
     - `copy_node.random = hashmap[original_node.random]`
   - Since all nodes are already created in the first pass, this step links the nodes correctly.

3. **Return the copied head**:
   - Return the head node from the hashmap (`hashmap[head]`), as it is the head of the deep-copied linked list.

#### 3. **Time and Space Complexity**:
   - This approach works in **O(n)** time, as we traverse the list twice.
   - The space complexity is also **O(n)** due to the additional space used for the hashmap.

### Self Notes
To achieve this we can use basic traversal of linked list along with hashmap, but need to do traverse the list twice, 1st - to create copy nodes & save to hashmap, 2nd to make next & random connection to nodes.
every node has two values, val -- indicates current value & next -- links to next value. since we're asked to create a deep copy aka an exact new copy list. in the first pass, create a copy node for each node & add this copy to hashmap for the original node in format original node: copy node. in the second pass, we get the copy node from hashmap for original node & replicate connections for next & random since those nodes are already created in the first loop. in the end return head node's value from hashmap since that's the copy list's first node


```
"""
   use basic linked list traversal along with a hashmap to solve the problem
      trick is to traver list 2 times 
         1st -- to create copy nodes & save them to hashmap
         2nd -- to make next & random connections to nodes 

   first pass
   loop thru the list
      create a copy node for each node
      add copy node to hashmap for the original node -- original node: copy node

   second pass
   loop thru the list
      get copy node from hashmap for curr node i.e original node
      replicate next & random connection of the original node to the copy node
         can do it by accessing those nodes from hashmap as well

   in the end return head's node value from hashmap since that's copy list's first node 
"""
```