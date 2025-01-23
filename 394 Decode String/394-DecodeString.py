class Solution:
    """
    this is a classic stack problem
        we need to process things in stack in a certain manner
        get the characters to be repeated 
        get the number of times those chars have to be repeated
        insert all values into the stack
        once a closing brace has been encountered
            we need to process the last string
            find all chars until a [ is hit -- last point for current chars
            find all nums until a char is hit -- last point for current nums
            repeat char num times & add to stack
        do this until the end, we have our result in the stack
    """
    def decodeString(self, s: str) -> str:
        # create stack
        stack = []

        # loop for each char in string
        for c in s:
            # check if current char is closing brace, means we need to decode last string
            if c == ']':
                # get chars
                chars = "" # variable to store current iteration characters
                # loop while stack isn't empty and current variable is not [ -- means that's the end
                while stack and stack[-1] != '[': #.isdigit():
                    # add current char to chars
                    chars = stack.pop() + chars

                # pop once from stack to get rid of [
                stack.pop()

                # get numerics
                num = "" # variable to store current iteration number
                # loop while stack isn't empty and current variable is a digit -- means that's the end
                while stack and stack[-1].isdigit():
                    # add number to numbers -- traversing in reverse order
                    num = stack.pop() + num

                # multiply & insert into stack
                stack.append(int(num) * chars)
            else:
                # append to stack
                stack.append(c)

        # return values in stack joined together
        return ''.join(stack)
