# 67. Add Binary

1 possible solution for this problem  


```
"""
    we can solve this using basic bit by bit computation
        the idea is to add values using bit computation
            since the operation is addition
            0 + 0 = 0
            1 + 0 = 1 & vice versa
            1 + 1 = 0 & carry 1 to next digit
        to apply above computation, we need to process input values digit by digit & get actual number values
        
        to solve the problem, reverse the input arrays
            process each digit
            get value of each digit by converting to int -- since input is str
            add these int values & carry to get current value
            since the output should also stay in binary, we implement below steps to convert to binary
                mod total value to get value at current location -- %
                divide total value to get carry value for next location -- //
            add the current location value to output result
            update carry value for next iteration

        since we're processing inputs in reverse order, return output after reversing -- makes it the correct order
"""
```

