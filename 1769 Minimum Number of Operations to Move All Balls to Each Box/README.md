# 1769. Minimum Number of Operations to Move All Balls to Each Box

1 possible solution for this problem  

### Self Notes


```
"""
    This solution uses two pointers, prefix sum, dynamic state tracking
        the solution requires keeping track of the no. of moves required to move balls at any index
        to achieve this, we need to know the no. of balls to left & right & no. of moves those balls make
    
    take 4 variables that track
        balls - to left & right -- 2 variables
        moves - to left & right -- 2 variables
    
    loop thru the length of input
        simultaenously calculate the no. of balls & moves at any particular index from either side
            left to right --> i
            right to left --> n - 1 - i
                gives index of current right pointer from last
        add current location value to balls 
        add no. of balls to moves at every index
            simulating moves each ball for every index
        if we add both left & right values, we get the total moves required for that index
"""
```

