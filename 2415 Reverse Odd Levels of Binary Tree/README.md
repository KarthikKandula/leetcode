# 2415. Reverse Odd Levels of Binary Tree

1 possible solution for this problem  

### Self Notes


```
"""
    this is a classic slow & fast pointer problem
        move the pointers in below method
            move slow pointer by one hop
            move fast pointer by two hops
        loop while fast & fast.next isn't none
        once the loop ends, the slow pointer is pointing at the mid of linked list
"""
```

