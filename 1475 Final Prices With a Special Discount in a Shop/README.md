# 1475. Final Prices With a Special Discount in a Shop

1 possible solution for this problem  

### Self Notes


```
"""
    Stack solution

    we can solve this problem using stack (monotonic stack)
        since we need to find the lowest index that satisfies a condition
        we can insert indexes into the stack instead of the actual values
        update values in the input array when the latest value from stack is greater than the current loop value
    
    loop thru input array
        check if last value in stack is greater than or equal to the current looped value
            if it is, reduce the value by the current looped value
        insert current index into the stack
    
    once all elements have been visited, answer array is saved in the input array
"""
```

