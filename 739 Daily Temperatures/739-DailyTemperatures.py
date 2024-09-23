class Solution:
    """
    Use stack (monotonic stack) to solve the problem
        It's not a prefix implementation in python, we make it monotonic in our code - it means values are always in decreasing order

    Create two arrays (stacks) 
        one for storing the values as we traverse thru them
        other for storing the output result

    loop thru the input temperatures
        check if there are any values in the stack that are less than current temperature (in a while loop)
            if there are, we have the answer for that index
                pop the value, update the index of popped value - subtract it with the current index
            do it until there are no values less than current in the stack
        if there are no values less than current, append current value to the stack
            append in the format (temperature, index) - use to subtract index value with current index while updating result array
    once traversed thru all the input, output is in result array
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # # Initialize stack (monotonic stack) - save in this stack as a pair (temperature , index)
        res = [0] * len(temperatures) # output array - same length as input temperatures w/ default values

        # Loop through input temperatures
        for i, val in enumerate(temperatures):
            # if any previous values in stack are less than current temp, a higher temp has been found, can update the result
            while stack and val > stack[-1][0]:
                # Pop values less than current, popping this way assigns each value to each variable
                tempVal, tempIndex = stack.pop()
                # save difference of popped index & current index in output array in popped index location
                res[tempIndex] = i - tempIndex

            # Append current [temperature, index] for next processing
            stack.append((val, i))

        # return result variable
        return res
