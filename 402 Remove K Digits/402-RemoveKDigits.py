class Solution:
    """
    this is a classic mono decreasing problem with a couple twists
        since we need to remove k digits to make the value as low as possible
        we remove values that are out of place
            i.e., where their next values are greater
            since this value is high than it's next, we remove it the value comes down the most compared to others
        to implement this, we can use mono decreasing stack to implement
            remove values from stack and decrement k values 
                to only remove k digits
            handle the leading 0's edge case by not inserting into stack when it's empty
        in the end, combine all values from stack and return
    """
    def removeKdigits(self, num: str, k: int) -> str:
        # mono decreasing stack
        stack = []

        # loop for each element in input
        for i, v in enumerate(num):
            # remove higher elements from stack -- classic mono dec stack impl
            while k > 0 and stack and int(v) < int(num[stack[-1]]):
                stack.pop() # pop from stack
                k -= 1 # decrement no. of operations
            
            # additional use case -- if stack is empty and value is 0, don't insert
            if not stack and v == '0':
                continue

            # append to stack
            stack.append(i)

        # create result variable
        res = ""

        # loop for length of stack, if any values are remaining in k, remove those values from the end
        for i in range(len(stack) - k):
            # append value from stack to result 
            res += num[stack[i]]
        
        # return result, else string with 0
        return res if res else '0'

