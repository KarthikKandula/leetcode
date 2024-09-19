# 3. Longest Substring Without Repeating Characters

1 possible solution for this problem

## Method 1

We can solve this problem using the **sliding window** approach:

1. **Initialize two pointers**: Both `left` and `right` start at the beginning of the string.
2. **Track characters**: Use a set to store unique characters from the current substring.
3. **Expand the window**: Move the `right` pointer forward, adding characters to the set as long as they are unique.
4. **Handle duplicates**: When a duplicate is found, remove the character at the `left` pointer from the set, then increment `left` to shrink the window. Repeat this until the substring is unique again.
5. **Continue until the end**: Repeat the process until the `right` pointer reaches the end of the string.

This efficiently identifies the longest substring without repeating characters.

### Self Notes
The problem statement asks us to go thru the input array & find the longest substring without repeating characters.  
To achieve this we can use the sliding window method with a little twist. Assign two pointers to the same initial value, here right pointer moves forward & left pointer stays at the start of the unique substring. Use a set to record all the visited values until now. As soon as the right pointer hits a value already in set (duplicate has appeared), remove that value along with everything before it & reassign the left pointer in the process. Continue doing it until the end.  

```
"""
    Use two pointer sliding window method to solve the problem
        doing this we get to compare each variable with each other

    Use two pointers - buy & sell assigned to 0th & 1st index respectively
        so we get to go thru the entire input in a sliding window method
    
    Loop thru input as long as sell < length of input
        calculate profit & replace maxProfit along the way
        check if sell price is less than buy price
            if yes, we have found a new low price to buy
        increment sell in each iteration to compare next price
"""
```
