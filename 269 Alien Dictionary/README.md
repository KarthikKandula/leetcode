# 269. Alien Dictionary

1 possible solution for this problem  

## Method 1

## Problem Intuition
The goal is to determine the order of letters in an alien language based on a given list of words sorted lexicographically. This can be solved by building a graph where:
- Nodes represent letters.
- Directed edges represent precedence between letters.
  
The problem boils down to performing a **topological sort** on the graph. If a valid order exists, return it; otherwise, return an empty string.

## Approach

### Key Idea
1. **Build the Graph**:
   - Construct an adjacency list to represent the graph based on letter precedence derived from the input words.
   - Handle edge cases such as invalid input with mismatched prefixes.
2. **Perform Topological Sort**:
   - Use DFS with cycle detection to determine the correct letter order or detect if no valid order exists.

### Step-by-Step Solution

1. **Build the Adjacency List**:
   - Initialize a hashmap `adjList` where each letter maps to a set of letters that must come after it.
   - Populate the adjacency list by comparing consecutive words in the input:
     - For each pair of words:
       - Find the minimum length of the two words.
       - If the first word is longer and has the same prefix as the second, return an empty string (invalid order).
       - Otherwise, find the first mismatched character between the two words and update the adjacency list:
         - Add an edge from the first mismatched character in the first word to the second word.

2. **Prepare for Topological Sort**:
   - Create a `visited` hashmap with three states:
     - `True`: The node is currently in the DFS path (cycle detection).
     - `False`: The node has been visited but is not in the current DFS path.
     - Not in `visited`: The node has not been visited.
   - Initialize a `result` list to store the topological order.

3. **Implement DFS Helper Function**:
   - **Input**: A letter (node).
   - **Base Case**:
     - If the letter is already visited:
       - If its value is `True`, a cycle is detected; return `True`.
       - If its value is `False`, skip further processing and return `False`.
   - **Process the Current Letter**:
     - Mark the letter as `True` in `visited` to indicate it’s in the current DFS path.
     - For each neighbor of the letter in `adjList`:
       - Recursively call the DFS function. If any call detects a cycle, return `True`.
     - After visiting all neighbors, mark the letter as `False` in `visited` and append it to `result`.

4. **Perform Topological Sort**:
   - For each letter in `adjList`, call the DFS function:
     - If any DFS call returns `True`, it means a cycle exists, and the input is invalid; return an empty string.

5. **Return the Result**:
   - If the graph is a valid DAG, reverse the `result` list (to account for post-order DFS traversal) and convert it to a string.

### Summary
- **Topological Sort Logic**: The result is built by appending letters only after visiting all their neighbors. This ensures the order respects precedence constraints.
- **Cycle Detection**: The `visited` hashmap with `True` values helps detect cycles during DFS traversal.
- **Output**: Return the reversed `result` as the valid order or an empty string if no valid order exists.

### Self Notes

```
"""
   use Topological Sort to solve the problem
      entire problem is dependent on the order of alphabets as appeared in the input 
      and figuring out the difference in order & returning them in lexicographically increasing order
      to achieve this, if we first build out a graph in the order of how the letters appear
         then we can traverse thru the graph & easily create the order in which the letter appear
   
   to apply topological sort to this problem, we need to build an adjacency list first
   create an hashmap with all letters that appear in the input
   building adjaceny list
      we'll compare any two words at once
      get the minlength of the two words in consideration
      we check for the condition -- if the first appearing letter has length more than second with same prefix
         acc to the problem desc, this is invalid
         if this occurs, return empty string since an order can't be established
         since if the first word has more letters with same prefix it's not possible to establish a relationship
      now, loop thru the minlength of both words & compare each letter
      on the first mismatch, add the mismatch to adjacency list
         the letter from first word comes before letter from second word
         hence add letter from second word to the value in letter from first word
      
   create a visited hashmap -- empty at first
      a hashmap in this case since we have multiple conditions to take care in terms of visited
      two values 
         False -- means this value has already been visited, this is not bad necessarily
         True -- means this value is visited & in current path, this will help in finding cycles
         if not in hashmap -- means a new value
   
   create a result array

   create a helper function implemented recursively
      input is the letter
      check for base condition
         if this letter has already been visited
            return the value from visited hashmap
      if reaches this point, it means it hasn't been visited & is a new letter
      assign value true to this letter in visited set
      now loop for each neighbor in adjacency list for this letter
         recursively call for each neighbor
         if any neighbor returns true -- it means there's a cycle, we return true
      change value to false for this letter in visited set
         not in current path anymore
      append this letter to result array
   
   loop thru each char in adjacencylist 
      call recursive function for each char
      if any function returns true, it means there a cycle & we return ""
      since there's no possibility of a solution
   
   if a solution is possible we can return the reversed out result array converted to a string
      solution is in reversed order since appending to result array only after all neighbors are visited
      this is the Kahn's algorithm aka topological sort
"""
```
