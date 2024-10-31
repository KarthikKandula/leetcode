# 212. Word Search II

1 possible solution for this problem  

## Method 1

## Problem Intuition
In this problem, we are given a board of characters and a list of words. We need to find which words from the list can be formed by tracing a continuous sequence of adjacent letters (horizontally or vertically) on the board. A naive solution would perform a depth-first search (DFS) for each word, which is inefficient. Instead, we can optimize using a Trie and backtracking.

**Key Optimization**:
1. Use a **Trie** to store all the words, reducing redundant search operations.
2. Perform DFS only on positions that have a matching prefix in the Trie, significantly reducing the number of recursive calls.

## Approach

### Step 1: Build a Trie
1. **Create a root node** for the Trie.
2. **Add all words** from the list into the Trie. This helps in efficiently checking prefixes during the DFS search.

### Step 2: Iterate Through the Board
- Loop through all rows and columns of the board.
- For each position, check if the character exists in the Trie. If it does, call the recursive DFS helper function.

### Step 3: Define the Recursive DFS Helper Function
The DFS function will recursively explore all possible paths from a given starting point.

1. **Input Parameters**: Current row, column, the current Trie node, and the current string that matches the Trie so far.
2. **Base Case Checks**:
   - If the current row or column is out of bounds, return.
   - If the current position has already been visited, return.
   - If the character at the current board position does not exist in the Trie at the current node, return.

3. **Proceed If All Checks Pass**:
   - Add the current position to the visited set.
   - Move to the next Trie node that matches the current board character.
   - Append the current board character to the word being formed.
   - If the current Trie node is marked as the end of a word, add the word to the result set.

4. **Recursive Calls for Adjacent Positions**:
   - Perform recursive DFS for all four adjacent positions (up, down, left, right).

5. **Backtrack (Cleanup)**:
   - Remove the current position from the visited set to allow future recursive operations to explore other paths.

### Step 4: Return the Result
- Convert the result set to a list and return it after all recursive calls are completed.

### Self Notes

```
"""
   this problem is similar to word search but here words are given to us
      need to find which words appear in board
   
   if we implement a recursive dfs function, we need to implement dfs for each word
      that multiplies it by the number of words given to us
   
   to implement it in a more efficient manner
      we can first create a trie for the words
      loop thru each position from the board & check if that value exists in the trie
         if it does, recursive call for adjacent nodes with the next node's value
         if it doesn't return from function 
               so essentially only hitting a position if it exists in the trie
               reduces on the number of recursive calls
   
   create a root node for trie
      add all words to trie

   loop thru all rows & colums
      recursively call helper function for each position in board

   create a helper function that implements dfs recursively
      input is row, column, trie's node that we're searching & the current string that matched from trie so far
      check if row, column are out of bounds
         return from function
      check if row, column exists in visited
         return from function
      check if current value in board exists in trie at current node
         return from function
      
      at this point in the program, it means we're in the right direction to find a word

      add current position to visited
      update node from trie to the new node
         since it matched with current board's position
      update word
         add current board's position to it
      if current node is marked as end of word
         add it to result
      
      recursively call for all 4 adjacent positions
      
      cleanup current position from visited -- for future recursion ops

   after all recursive functions return, result is in result set, return it as a list
"""
```
