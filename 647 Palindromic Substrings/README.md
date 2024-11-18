# 647. Palindromic Substrings

1 possible solution for this problem  

## Method 1

## Problem Intuition
The task is to count all palindromic substrings in a given string. A substring is a palindrome if it reads the same forwards and backwards. This can be efficiently solved using a two-pointer approach that expands around each character or pair of characters as a potential center.

### Key Insight
1. **Expand Around Center**:
   - Treat each character and each pair of adjacent characters as a potential center of a palindrome.
   - Expand outward while the characters at the left and right pointers match, counting valid palindromes.

## Approach

### Step-by-Step Solution

1. **Define Helper Function for Expansion**:
   - A function `countPali(s, l, r)` to count palindromes centered at indices `l` and `r`:
     - **Input**: String `s`, and pointers `l` and `r`.
     - **Logic**:
       - While `l` and `r` are within bounds and `s[l] == s[r]`:
         - Increment the palindrome count by 1 (a valid palindrome is found).
         - Expand outward by decrementing `l` and incrementing `r`.
     - **Output**: The count of palindromes found for this center.

2. **Iterate Through Each Character**:
   - For each index `i` in the string:
     - Count odd-length palindromes:
       ```plaintext
       result += countPali(s, i, i)  # Centered at a single character
       ```
     - Count even-length palindromes:
       ```plaintext
       result += countPali(s, i, i + 1)  # Centered between two characters
       ```

3. **Aggregate the Results**:
   - Maintain a `result` variable to store the total count of palindromic substrings.
   - Add the counts from both odd-length and even-length palindrome checks for each center.

4. **Return the Result**:
   - Return `result` after iterating through all possible centers.

### Example Walkthrough
For input `"abc"`:
- Odd-length palindromes:
  - `'a'`, `'b'`, `'c'` → 3 palindromes.
- Even-length palindromes:
  - None.

For input `"aaa"`:
- Odd-length palindromes:
  - `'a'`, `'a'`, `'a'`, `'aaa'` → 6 palindromes.
- Even-length palindromes:
  - `'aa'`, `'aa'` → 2 palindromes.

### Summary
- **Expand Around Center Logic**: By expanding outward from each character (and pair of characters), we efficiently count all palindromic substrings.
- **Efficiency**:
  - **Time Complexity**: `O(n^2)`, as each expansion takes `O(n)` and we iterate through `n` characters.
  - **Space Complexity**: `O(1)`, as no additional space is used apart from variables for counting.
- **Output**: The function returns the total count of palindromic substrings in the input string.


### Self Notes


```
"""
   we can treat this as a two-pointer expansion problem
      the goal is to count all palindromic substrings in the input string
      a substring is a palindrome if it reads the same forwards and backwards
      to count all palindromes, we explore around each character in the string as a potential center

   create a helper function `countPali` to count palindromes centered at a given pair of indices (l, r)
      input is the string `s`, and two pointers `l` and `r` representing the center
      while `l` and `r` are in bounds and the characters match, increment the result count
      move the left pointer leftward (l -= 1)
      move the right pointer rightward (r += 1)
      return the count of palindromes found for this center

   loop through each character in the string as a potential center for palindromes
      for each index `i`:
      perform two operations:
         count odd-length palindromes using `countPali` with the center at `i` (l = r = i)
         count even-length palindromes using `countPali` with the center between `i` and `i + 1` (l = i, r = i + 1)
      add the counts from both operations to the total result

   return the total result as the number of palindromic substrings in the input string
"""
```
