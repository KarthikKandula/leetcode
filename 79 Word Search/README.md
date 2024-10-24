# 79. Word Search

1 possible solution for this problem  

## Method 1

We can solve this problem using a combination of a set and backtracking. The recursive approach efficiently explores all possible paths to find the target word, while the set helps in avoiding revisiting the same location.

### Steps

1. **Concept Overview**:
   - The solution requires exploring the entire grid to find a target word. This involves recursive exploration of each character and path in the grid.
   - We use a set to keep track of visited positions and avoid cycles, ensuring we do not revisit the same location twice.

2. **Recursive Function**:
   - **Input Parameters**: The recursive function takes the current row, column, and the current index in the target word being searched.
   - **Conditions to Check**:
     1. **Word Found**: If the current index equals the length of the word, return `True` since the entire word has been found.
     2. **Out of Bounds**: If the current row or column is outside the grid boundaries, return `False`.
     3. **Character Mismatch**: If the current grid cell does not match the character at the current index of the word, or if the cell is already in the set (visited), return `False`.

3. **Recursive Exploration**:
   - If none of the above conditions are met, add the current position `(row, col)` to the set (mark as visited).
   - Make recursive calls in all four possible directions: top, bottom, left, and right.
   - **Backtrack**: After exploring all possible directions, remove the current position from the set to allow other recursive paths to explore it independently.

4. **Return Condition**:
   - Use an OR condition to return the result of the recursive calls. If any of the recursive calls return `True`, the function should return `True`.

5. **Loop Through the Grid**:
   - Outside of the recursive function, loop through each cell in the grid (rows and columns).
   - Call the recursive function from each starting position in the grid. If any of these calls return `True`, return `True` as the final answer. Otherwise, return `False`.

### Summary

The solution efficiently explores all possible paths using backtracking with a set to track visited positions. By checking all possible directions recursively and using an OR condition for the return values, the algorithm ensures that we find the target word if it exists in the grid.


### Self Notes
We can use set with backtracking to solve the problem in an effective manner. in backtracking we'll use recursive function to explore all possibilites. Since we need to explore the entire input, we need to implement a recursive function which makes it easy to explore all possibilities. use set to avoid visiting any location twice. input for recursive function is row, col positions & the current index in the word we're trying to search. The recursive function depends on few conditions, 1. if current word index is equal to length of word -- true condition 2. if row & col are in bounds -- false condition, 3. if current location row, cols is not equal to current word's index and if row, col exists in set -- false condition. if none of the above conditions are met, we need to keep looking, add current position to set, make recursive calls for each direction i.e., top, bottom, back, front. remove current location from set -- to not affect other recrusive stacks. return based on return values from recursive calls -- it's an or condition, if one value is true, return true. 

outside this recursive function, loop thru rows & cols & call for each position. if any return value is true, return true. else False 

```
"""
   use backtracking to solve this problem
      acc to the problem description, we get certain understanding
      we have to visit all horizontally & vertically neighboring cells i.e., top, bottom, back, front
   
   take a set that keeps track of all locations visited for the current recursive trace
   call the recursive function for each position in the input

   create a hepler function that is implemented recursively
      input for this function is row, col positions & the current index in the word we're trying to search
      check if current word index is equal to the length of word 
         return true since we've found the word -- it wouldn't reach to this point if all other values didn't match
      check if current location is in bounds
         return false if not - row & col values has to be within input's bounds
      check if current location is equal to the current word's index
         return false if not
      add current location to path set
      make recursive calls for each direction i.e., top, bottom, back, front
      remove current location from path set -- to not affect other recursive stacks
      
      return true or false based on the return values from recursive calls
         it's an or condition, if one value is true we return true
      
   loop thru rows & cols of input & recursively call helper function for each location
      if returns true, return true -- word is found
   
   return False at end -- if true isn't returned above, word doesn't exist in input
"""
```
