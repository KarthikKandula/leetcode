# 17. Letter Combinations of a Phone Number

1 possible solution for this problem  

## Method 1

## Problem Intuition
In this problem, we are given a string of digits, each mapping to a set of letters on a traditional phone keypad. The task is to generate all possible letter combinations that the number could represent. This is a classic combinatorial problem well-suited for backtracking.

**Recognizing the Problem**:
1. **Combinatorial Exploration**: The problem involves generating all possible letter combinations for each digit.
2. **Choice at Each Step**: Each digit offers multiple choices (letters), suggesting a recursive exploration pattern.

## Approach
### Step 1: Create a Helper Function
The helper function will recursively build letter combinations from the given digits.

- **Input**: The current index in the input digit string and the current string being formed.

### Step 2: Define the Base Case
- If the length of the current string equals the length of the input digits:
  - Append the current string to the result array, as it forms a complete combination.
  - Return from the function to stop further recursion on this path.

### Step 3: Iterate Over Possible Characters for Each Digit
- Loop through all the letters corresponding to the current digit (using a pre-defined mapping or hashmap).
- For each letter:
  - Recursively call the helper function with:
    - The next index in the input digit string.
    - The current string appended with the chosen letter.

### Step 4: Return the Result Array
- Once all recursive calls are completed, the result array will contain all valid letter combinations.
- Return the result array as the final solution.

### Note:
In this problem, there’s no need to explicitly clean up or backtrack the current string after each recursive call, as strings are immutable in most programming languages. This makes the approach more efficient and simple.


### Self Notes


```
"""
   neetcode solution

   use backtracking to solve the problem
      need to compile all possible combinations to generate all possible strings
   
   create a helper function that is implemented recursively
      input to this function is current index in input & current string
      check if length of current string is equal to length of digits -- base case
         append current string to result array -- found a candidate
         return from function
      loop thru all the letters at that digit (retrieve from hashmap)
         recursively call for next index along with updated curr string
      since we don't need to do this is a list of list manner, don't have to clean current string for future operations
         usually a constant in backtracking problems but not required in this
   
   once all recursive ops are done, result is in the result array, return it
"""
```
