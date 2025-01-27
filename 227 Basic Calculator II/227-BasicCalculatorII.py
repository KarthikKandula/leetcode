class Solution:
    """
    we use a stack to solve this problem
        the basic idea is to solve multiplication and division first, so it's solved immediately
        when encountering a + or - operator
            insert the num with the sign into the stack 
        so that the numbers are in stack with their sign
            once multiplication & division are solved
            sum the values in stack & we get the answer
    """
    def calculate(self, s: str) -> int:
        num = 0 # to keep tracking recent num
        s += '+' # add + at end to process everything at end
        prevOp = '+' # assign a neutralizing prevOp at start 
        stack = [] # stack to track recent values

        # loop for each value in input s
        for i in range(len(s)):
            # get char at curr index
            c = s[i]

            # if c is a digit
            if c.isdigit():
                # update num value
                num = (num * 10) + int(c)
            
            # if c is a symbol +-*/
            elif c in '+-*/':
                # if previous operand is +
                if prevOp == '+':
                    # append to stack
                    stack.append(num)
                # if previous operand is -
                elif prevOp == '-':
                    # append to stack
                    stack.append(-num)
                # if previous operand is *
                elif prevOp == '*':
                    # pop from stack & multiply current num, place back in stack
                    stack.append(stack.pop() * num)
                # if previous operand is /
                elif prevOp == '/':
                    # pop from stack & divide current num, place back in stack
                    stack.append(math.trunc(stack.pop() / num))
                
                num = 0 # reset num if a symbol is seen
                prevOp = c # update current operand as previous operanc

        # return a sum of values in stack 
        return sum(stack)


class Solution:
    def calculate(self, s: str) -> int:
        
        if len(s) <= 1:
            return int(s)

        s = s.strip()

        num = 0

        stack = []

        solve = False

        for i in range(len(s)):
            c = s[i]
            # print(c, num, stack)
            # if c is a digit
            if c.isdigit():
                num = (num * 10) + int(c)
                # stack.append(c)
            
            # if c is * or /
            elif c in '*/':
                stack.append(num)
                num = 0

                # if we need to solve this equation -- only for * & /
                if solve:
                    num2 = stack.pop()
                    sign = stack.pop()
                    num1 = stack.pop()

                    res = self.solveEquation(int(num1), sign, int(num2))
                    stack.append(res)

                    solve = False

                stack.append(c)

                solve = True

            # if c is + or -
            elif c in '+-':
                stack.append(num)
                num = 0

                # if we need to solve this equation -- only for * & /
                if solve:
                    num2 = stack.pop()
                    sign = stack.pop()
                    num1 = stack.pop()

                    res = self.solveEquation(int(num1), sign, int(num2))
                    stack.append(res)

                    solve = False

                stack.append(c)
            
            # print(f"{c} {num} {stack}--")
        
        if num != 0:
            stack.append(num)
        
        print(stack)

        # at this point all * & / operators are solved
        # now solve for + & -
        while len(stack) > 1:
            num2 = stack.pop()
            sign = stack.pop()
            num1 = stack.pop()

            res = self.solveEquation(int(num1), sign, int(num2))
            stack.append(res)

        print(stack)

        return stack[0]
    
    def solveEquation(self, num1, sign, num2):
        if sign == '+':
            return num1 + num2
        elif sign == '-':
            return num1 - num2
        elif sign == '*':
            return num1 * num2
        elif sign == '/':
            return num1 // num2
