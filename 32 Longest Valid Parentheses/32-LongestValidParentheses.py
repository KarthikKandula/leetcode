class Solution:
    """
    we can solve this problem using monotonic stack
        use the stack to track ( values
        if a ) value is encountered, it removes a corresponding ( from the stack
        if a ) has no matching (, pops value & makes stack empty
            now we insert current index which is the boundary for any future calculations
    """
    def longestValidParentheses(self, s: str) -> int:
        # create stack with -1 to initialize a value
        stack = [-1]

        # variable to track max count
        maxCount = 0

        # loop for each index in input
        for i in range(len(s)):
            # if cur val is (
            if s[i] == '(':
                # append to stack
                stack.append(i)
            # if cur val is )
            else:
                # pop from stack
                stack.pop()

                # if stack is empty after pop
                if not stack:
                    # add current index to stack
                    stack.append(i)
                #If stack isn't empty
                else:
                    # calculate max distance to valid paranthesis
                    maxCount = max(maxCount, i - stack[-1])
        
        # return max value
        return maxCount 

    """
    Own solution -- not working
    """
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = []

    #     res = 0
    #     count = 0

    #     for c in s:
    #         if c == ')':
    #             if stack and stack[-1][0] == '(':
    #                 stack.pop()
    #                 count += 2
    #                 res = max(res, count)
    #             else:
    #                 count = 0
    #                 stack.append((c, max(res, count)))
    #         else:
    #             # if stack and stack[-1][0] == '(':
    #             #     count = 0
    #             stack.append((c, max(res, count)))

    #     print(stack)
    #     for c, v in stack:
    #         res = max(res, v)

    #     return res