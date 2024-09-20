# 76. Minimum Window Substring

1 possible solution for this problem

## Method 1

We can solve this problem using the **sliding window** approach with two hashmaps:

1. **Initialize two hashmaps**: 
   - One for counting the characters in the first string (required characters).
   - Another for tracking the characters in the current window of the second string.
2. **Set up `have` and `need` pointers**:
   - `have`: Tracks how many required characters we currently have in our window.
   - `need`: The total number of distinct characters needed from the first string.
3. **Iterate through the second string**:
   - As you expand the window by moving the `right` pointer, update the counts in the second hashmap and adjust the `have` pointer accordingly.
4. **Check for a valid window**:
   - If `have == need`, the current window contains all required characters. Now, try to minimize the window by incrementing the `left` pointer while maintaining the required characters.
5. **Track the minimum window**:
   - Each time you find a valid window, check if it's the smallest so far and update the result variables accordingly.
6. **Continue until the end**: Repeat this process until the `right` pointer reaches the end of the second string.

This approach efficiently finds the minimum window substring by managing the `have` and `need` pointers and updating the result as the window changes.

### Self Notes
To achieve this we can use the sliding window method approach. There are two inputs, take two hashmaps to keep track of counts of each input strings. first, go thru the first string to get counts of each letter. while going thru the second string, create have & need pointers where have is the count of letters we currently have in our window & need is the count of letters we require.  
If at any time these both values are equal, current window has all the values we require, start decreasing the window since objective is to find the minimum window substring. by handling have & need accurately & storing the result in result variables, we get the solution

```
"""
    Use sliding window approach to solve the problem
        in a nutshell the problem is to find the smallest substring that has all letters from t in s, can also have other letters
        and the return value is the actual substring itself

    First, we get a count of every letter in t

    Loop thru string s - using your right pointer
        left & right pointers are in the same location
        have two variables have & need
            have - is the count of letters from t we currently have in our window in this iteration of s
            need - is the count of letters from t we're required to have
        As looping thru the input s string, increment have as you find variables in t - ignore for the other letters

        check if at any time have == need, 
            if they are it means in the current window we have all the letters from t
            but since our objective is to find the minimum substring, start removing letters from left pointer
            update the result length & start & end index of current window as you go
            and if at any point you eat into something in the have string, decrement accordingly

    loop thru the end of the string
        the final result length & start, end index of substring is in the result variables 
"""
```