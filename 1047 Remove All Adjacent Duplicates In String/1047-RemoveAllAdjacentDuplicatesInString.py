class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [] # stack to process values

        # loop thru each char in input
        for i, c in enumerate(s):
            # check if stack is populated and prev value is equal to curr value
            if stack and c == s[stack[-1]]:
                stack.pop() # pop last value from stack
            # if prev value is not equal to current
            else:
                stack.append(i) #insert into stack

        # create result variable
        res = ""

        # loop for values in stack
        for i in stack:
            # append to result variable
            res += s[i]

        # return result value
        return res
