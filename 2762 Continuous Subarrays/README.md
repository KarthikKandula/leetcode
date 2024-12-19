# 2762. Continuous Subarrays

1 possible solution for this problem  

### Self Notes


```
"""
    use sliding window & two pointers to solve the problem
        the condition is to count the num of subarrays with diff btwn max and min values less than or equal to 2
        since it's asking for subarrays in an array -- it's a sliding window problem
            since the window length is variable, it's a varible sliding window problem 
            we should use two pointers

        we need to maintain min & max values all the time for the current window
            to do this we use two deques
                minQ - stores indexes of elements in increasing order of their values
                    so that nums[minQ[0]] is always smallest value in the window
                maxQ - stores indexes of elements in decreasing order of their values
                    so that nums[maxQ[0]] is always largest value in the window

        if the diff btwn max & min values (always in front of deques) exceeds 2
            increment left pointer
            remove any indexes from deque that are out of window

        for each window, num of subarrays between l and r is r - l + 1
"""
```

