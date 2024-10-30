# 131. Palindrome Partitioning

1 possible solution for this problem  

## Method 1

## Problem Intuition
When faced with a problem where you need to split a string into parts such that each part satisfies a certain condition (in this case, being a palindrome), backtracking often becomes a natural fit. The goal here is to explore all possible partitions and filter out those that meet the condition without changing the order of characters.

**Recognizing the Problem**:
1. **Key Constraints**: The problem asks for all possible solutions, which hints at a combinatorial exploration approach.
2. **Condition Verification**: Each partition needs to be checked against a specific condition (palindrome).
3. **Order Preservation**: The original order of the string must be maintained, which rules out reordering-based algorithms.
4. **Recursive Nature**: When a problem can be broken down into smaller subproblems that follow the same pattern, recursion (and by extension, backtracking) is typically an effective solution strategy.

## Approach
### Step 1: Create a Result Array
- **Result Array**: To store all the valid palindrome partitions.
- **Subset Array**: To keep track of the current partitions while exploring.

### Step 2: Define a Recursive Helper Function
The helper function will recursively explore all potential partitions starting from a given index.

- **Input**: Current index indicating the starting point for the recursive check.

### Step 3: Base Case Check
- If the index goes out of bounds:
  - Append the current subset to the result array, as it forms a valid partition.
  - Return to stop further recursion.

### Step 4: Iterate Over Possible Partitions
- Loop through each index from the current position to the end of the string.
- **For each substring**:
  - Check if the substring forms a palindrome using a separate helper function.
    - Example: If the current index is `1` and the end of the string is `4`, check substrings `[1-2]`, `[1-3]`, `[1-4]`, and so on.
  - If a substring is a palindrome:
    - Add it to the subset.
    - Recursively call the helper function with the next index.
  - After the recursive call, backtrack by removing the last added substring from the subset.

### Step 5: Return the Result Array
- After all recursive calls are complete, the result array will contain all valid palindromic partitions.
- Return the result array as the final solution.


### Self Notes


```
"""
   use backtracking to solve the problem
      we need to check all the possible combinations of palindrome's without changing the order of the letters in string
      we need to recursively check if a certain string is palindrome for each index till end of string
   
   create a result array & an array to keep track of all subset partitions

   create a helper function that is implemented recursively
      input to this function is the index at which we're performing current operation
      check if index is out of bounds
         append subset to result -- we've found one possible candidate
         return from function
      in a loop for each index from index to end of string
         check if each combination is palindrome -- create a helper function
               if index is 1, end of string is 4
                  check for 1-2, 1-3, 1-4
               if any string is palindrome, append to subset
               recursively call for next index -- same thing happens in that function as well
               clean up subset for future operations
   
   once all recursive functions are done, result is in the array, return it
"""
```
