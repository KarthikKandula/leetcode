# 211. Design Add and Search Words Data Structure

1 possible solution for this problem  

## Method 1

## Problem Intuition
We need to design a data structure that supports adding words and performing search queries. The search should be able to handle wildcard characters (`.`) that can match any letter. This makes it necessary to use a Trie for efficient word storage and recursive backtracking to handle the complexity of wildcard searches.

## Approach

### Trie Initialization (`__init__`)
- **Create a root node**: The root node is the starting point of the Trie. It contains a hashmap (`children`) for child nodes and a boolean flag `isWord` to mark the end of a valid word.

### Adding a Word (`addWord`)
1. **Loop through each letter** of the input word.
2. **Check if the letter exists** in the current node's hashmap (`children`):
   - If the letter exists, move to the next node.
   - If it does not exist, create a new node and assign it to the letter in the hashmap.
3. **Move the current pointer** (`curr`) to the newly created or existing node.
4. After processing all letters, set the `isWord` flag of the current node to `True` to mark the end of the word.

### Searching for a Word (`search`)
We use recursive backtracking to efficiently handle search queries, especially when wildcards (`.`) are present.

1. **Recursive Backtracking Helper Function**:
   - **Input**: The current index in the input word and the current Trie node.
   - **Loop through the word** starting from the given index:
     - If the current character is `.`:
       - **Wildcard Handling**: Loop through all child nodes in the current character's hashmap.
       - Recursively call the helper function for each child node with the next index.
       - If any recursive call returns `True`, return `True`. If none succeed, return `False`.
     - If the current character is a regular letter:
       - **Check if the letter exists** in the hashmap:
         - If it does not exist, return `False`.
       - Move the pointer to the next node.
   - At the end of the word, return the `isWord` flag of the last node to determine if the search was successful.

2. **Initial Call**: Make the first call to the helper function with index `0` and the root node.
   - The return value of this call is the result of the `search` function.

### Summary
- The `addWord` method efficiently inserts words into the Trie.
- The `search` method uses recursive backtracking to explore all possible paths when encountering a wildcard character (`.`).
- The combination of a Trie and backtracking ensures efficient word addition and complex search operations.

### Self Notes

```
__init__
"""
   create root node for trie
"""

addWord
"""
   to add a word
      loop thru each letter
      check if it exists in that hashmap
         if it does, do nothing
         if it doesn't, create a new node & assign to the letter in hashmap
      update curr to move to next node
      in the end, change isWord value to True
"""

search
"""
   use backtracking to solve search function
      we need to perform recursive backtracking for .'s since we have to consider all children nodes
      better to use recursive backtracking to implement searching for each child node
   
   create a helper function to implement recursive backtracking
      input to this function is the index from input word & the node to search
      loop for range index to end of input word
         if current letter is .
               loop thru all the nodes in current character hashmap
               recursive call for each node with next index
                  return True if any value is successful
               else return False
         if current letter is a letter
               check if it exists in hashmap
                  if it doesn't return false
               move pointer to next location
      in the end return the isWord value of last node

   make first recursive call for index 0 & root -- return value of this is search function's return value
"""
```
