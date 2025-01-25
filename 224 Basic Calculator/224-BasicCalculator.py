class Solution:
    """
    this implementation of basic calculator uses stack & some twists & turns
        the idea is to compute the value continuosly
        we need 3 variables to calculate the result efficiently
            res -- to store the running result
                as well as to seperate out the calcs for inside paranthesis ops
            num -- to store the current running number
                is reset when a possibility of new number exists
                aka a new sign/paranthesis
            sign -- to store the next numbers sign
    
    loop thru each value in the input string
        if current is digit
            add to num -- handle for multiple digits
        if current is a sign
            num has ended
                add this num to result with sign
            update sign for next number
            reset num -- for next number
        if current is a open paranthesis
            there are new possiblities, new calcs to be done
                we require fresh num, sign & res
            insert current res & sign into stack 
                storing them off -- will retreive when closing paranthesis
            reset res & sign -- for in paran ops
        if current is a closing paranthesis
            we need to calculate current paran values with prev values
            finish processing current num -- add to result
                will be the final in paran value
            get the sign, prev res from stack
            update res with prev values -- will be the overall result going forward
            reset num
        while returning, it's possible last value is a num
            so we perform one final adjusting to result before returning
    """
    def calculate(self, s: str) -> int:
        # create variables for common ops
        res = 0 # to store running result 
        num = 0 # to store current number
        sign = 1 # -1 - negative, 1 - positive

        # to store values while going into & out of paranthesis
        stack = []

        # loop for every char in input
        for i in range(len(s)):
            c = s[i]

            # if c is digit
            if c.isdigit():
                num = (num * 10) + int(c)

            # if c is a sign
            elif c in '-+':
                # finish calculating number until now
                res += (num * sign)

                # update sign
                sign = -1 if c == '-' else 1

                # reset num
                num = 0

            # if c is (
            elif c == '(':
                # insert result until now into stack
                stack.append(res)

                # insert sign into stack
                stack.append(sign)

                # reset res -- to calc inside paran vals
                res = 0

                # reset sign -- for inside paran ops
                sign = 1

            # is c is )
            elif c == ')':
                # process res until now
                res += (num * sign)

                # get sign from stack
                res *= stack.pop()

                # get prev res from stack
                res += stack.pop()

                # reset num for future ops
                num = 0

        # return value -- perform one final calculation
        return res + (num * sign)
