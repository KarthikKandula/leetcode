# 424. Longest Repeating Character Replacement

2 possible solutions for this problem
* both solutions using the sliding window problem, just a slight change in code approach

## Method 1

We can solve this problem using the **sliding window** approach:

1. **Initialize two pointers**: Both `left` and `right` start at the beginning of the string.
2. **Track character frequencies**: Use a hashmap to store the count of characters in the current substring.
3. **Expand the window**: Move the `right` pointer forward, updating the character count in the hashmap.
4. **Check the condition**: The core formula is:  
   `current_length - count_of_most_frequent_char <= k`
   - If this holds, continue expanding the window.
   - If not, decrement the character at the `left` pointer in the hashmap, and increment `left` to reduce the window size.
5. **Continue until the end**: Repeat the process until the `right` pointer reaches the end of the string.

This approach efficiently solves the problem by adjusting the window size based on the number of allowed character replacements (`k`).

### Self Notes
To achieve this we can use the sliding window method approach. Assign two pointers to the same initial value, here right pointer moves forward & left pointer stays at the start of the substring. Use a hashmap to record count of all visited values until now. The entire problem relies on the formula - current length - count of max appearing value <= k (acceptable char changes). As soon as this formula doesn't hold true, decrement the left pointer index value in count & increment left pointer to keep it moving. Continue doing it until the end.  

```
"""
    Use sliding window method to solve the problem

    The entire problem relies on the formula 
        current length - count of max appearing value <= k (acceptable char changes)

    Use a hashmap to keep count of the elements appearing in the input

    loop thru the input using the right pointer
        update count of elements in hashmap as they appear 
        check if the formula holds up
            if it doesn't - move the left pointer & decrement the count in hashmap
            if it does - update the result value

    by end of the loop, eventually the result variable will have the answer
"""
```

## Method 2

Exactly the above implementation but slight difference in the code.  

```
"""
    Use sliding window method to solve the problem

    The entire problem relies on the formula 
        current length - maxFrequency <= k (acceptable char changes)

    Use a hashmap to keep count of the elements appearing in the input
        slight modification is to create a new variable for maxFrequency

    loop thru the input using the right pointer
        update count of elements in hashmap as they appear 
        update maxFrequency with the current value of right pointer - eventually the value will have max value
        check if the formula holds up
            if it doesn't - move the left pointer & decrement the count in hashmap
            if it does - update the result value

    by end of the loop, eventually the result variable will have the answer
"""
```