# 5. Longest Palindromic Substring

1 possible solution for this problem  

## Method 1

## Problem Intuition
The task is to find the longest palindromic substring in a given string. A palindrome reads the same forwards and backwards. Instead of starting from the edges of potential substrings and working inward, this approach starts from the center of each potential palindrome and expands outward.

### Key Insight
1. **Expand Around Center**:
   - For each character in the string, check how large a palindrome can be formed by expanding outward.
   - Two cases must be handled:
     1. **Odd-Length Palindromes**: Centered at one character (`l = r = i`).
     2. **Even-Length Palindromes**: Centered between two characters (`l = i, r = i + 1`).
   - Track the longest palindrome encountered during these expansions.

## Approach

### Step-by-Step Solution

1. **Define Helper Function for Expansion**:
   - A function `expandAroundCenter(s, l, r)` to expand around the given center:
     - While `l` and `r` are within bounds and `s[l] == s[r]`:
       - Expand outward by decrementing `l` and incrementing `r`.
     - Return the substring `s[l+1:r]`, which represents the palindrome found.

2. **Iterate Through Each Character**:
   - For each character in the string (index `i`):
     - Check for the longest odd-length palindrome centered at `i` by calling `expandAroundCenter(s, i, i)`.
     - Check for the longest even-length palindrome centered at `i` and `i+1` by calling `expandAroundCenter(s, i, i+1)`.
     - Update the result if either palindrome is longer than the current longest palindrome.

3. **Track the Longest Palindrome**:
   - Maintain a `result` variable to store the longest palindrome found during the iterations.

4. **Return the Result**:
   - Return the `result` after iterating through all characters.

### Example Walkthrough
For input `"babad"`:
- At `i = 0` (`'b'`), expand for odd-length -> palindrome is `"b"`.
- At `i = 1` (`'a'`), expand for odd-length -> palindrome is `"aba"`.
- At `i = 2` (`'b'`), expand for odd-length -> palindrome is `"bab"`.
- Even-length expansions are also checked but do not exceed the odd-length result.

### Summary
- **Expand Around Center Logic**: By expanding outward from each character (or pair of characters), we reduce redundant checks and efficiently find palindromes.
- **Efficiency**:
  - **Time Complexity**: `O(n^2)`, as each expansion takes `O(n)` and we iterate through all `n` characters.
  - **Space Complexity**: `O(1)`, as no additional space is used apart from variables for tracking results.
- **Output**: The function returns the longest palindromic substring.


### Self Notes


```
"""
   we'd have to compare for palindromes for each substring in the given input
      instead of comparing from the outsides of a string & coming inwards
      let's put a simple twist
         let's check from inside -> out
         for every character, see how big of a palindrome can be formed by going out
         keep updating final result & result length variables as you go
         this way, the num of comparision are reduced

   the only downside of this approach is that
      We have to take two different approaches for this
         1. To check for odd length palindromes
               - We assign l, r = i 
         2. To check for even length palindromes
               - We assign l, r = i, i+1
"""
```
