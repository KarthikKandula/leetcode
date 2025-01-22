# 234. Palindrome Linked List

1 possible solution for this problem  


```
"""
    this is a basic linked list traversal problem with a couple twists
        to find if a string/number is palindrome we need to compare values from both sides
        in a linked list, going to end means we need to traverse the linked list
        best way to compare in efficient manner is
            get halfway point of the list
            reverse second half of the list
            compare each value from first half & second half of the list
                if a mismatch is found, return False
"""
```

