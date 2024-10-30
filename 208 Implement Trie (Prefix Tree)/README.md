# 208. Implement Trie (Prefix Tree)

1 possible solution for this problem  

## Method 1

## Problem Intuition
A Trie (Prefix Tree) is a tree-like data structure that stores words efficiently and allows for fast lookup operations. It is useful for scenarios involving prefix-based searches. Each node in the Trie represents a letter, and complete words are marked with a flag indicating the end of a word.

## Approach

### Trie Initialization (`__init__`)
- **Create a root node**: The root node serves as the starting point of the Trie. It doesn't store a character, but it holds a hashmap (`children`) to store subsequent letters.

### Inserting a Word (`insert`)
1. **Loop through each letter** of the input word.
2. **Check if the letter exists** in the current node's hashmap (`children`).
   - If the letter exists, move to the next node.
   - If it does not exist, create a new node and assign it to the letter in the hashmap.
3. **Move the current pointer** (`curr`) to the newly created or existing node.
4. After processing all the letters, mark the current node’s `isEndWord` flag as `True` to indicate the end of the word.

### Searching for a Word (`search`)
1. **Loop through each letter** of the input word.
2. **Check if the letter exists** in the current node's hashmap (`children`).
   - If it does not exist, return `False` as the word is not in the Trie.
3. **Move the current pointer** (`curr`) to the next node.
4. After processing all the letters, return the `isEndWord` flag of the last node. This flag indicates whether the word exists completely.

### Checking for a Prefix (`startsWith`)
1. **Loop through each letter** of the input prefix.
2. **Check if the letter exists** in the current node's hashmap (`children`).
   - If it does not exist, return `False` as no word with the given prefix exists in the Trie.
3. **Move the current pointer** (`curr`) to the next node.
4. After processing all the letters, return `True`. If the loop completes without returning `False`, it means all letters in the prefix exist.

### Summary
- The Trie structure effectively handles insertions, word searches, and prefix checks using hashmaps for each node.
- Each node maintains a hashmap for its child nodes and a boolean flag (`isEndWord`) to indicate the end of a word.

### Self Notes

```
__init__
"""
   create root node for trie
"""
insert
"""
   to insert a word
      loop thru each letter
      check if it exists in that hashmap
         if it does, do nothing
         if it doesn't, create a new node & assign to the letter in hashmap
      update curr to move to next node
      in the end, change isEndWord value to True
"""

search
"""
   to search a word
      loop thru each letter
      check if it exists in the hashmap
         if it doesn't, return False
      update curr to move to next node
      in the end, return isEndWord value -- of the last letter's node
"""

startsWith
"""
   to check if any word starts with a prefix
      loop thru each letter
      check if it exists in the hashmap
         if it doesn't, return False
      update curr to move to next node
      in the end, return True -- if the false condition isn't hit, means all letters exist
"""
```
