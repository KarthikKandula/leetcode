# 88. Merge Sorted Array

1 possible solution for this problem  

### Self Notes


```
"""
    solve this problem using two pointers but with a twist
        it's about comparing two numbers & sorting an array
        instead of doing it from start, better to do it from last to first
            offers flexibility & a bit neat code
        start two pointers at ends of each array
        start another pointer that tracks that current value to be replaced
        compare two pointer value & place the largest value at last pointer
            decrement accordingly
        once all values are processed, sorted array is in 1st input
"""
```

