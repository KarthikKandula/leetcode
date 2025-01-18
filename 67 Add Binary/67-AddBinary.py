class Solution:
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
    def addBinary(self, a: str, b: str) -> str:
        # variable to hold ouput result
        res = ""
        # variable to hold carry
        carry = 0

        # reverse input arrays to process starting from units digits -> outward
        a, b = a[::-1], b[::-1]

        # loop thru max length of input digits
        for i in range(max(len(a), len(b))):
            # get values at current index
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            
            # get values at current index
            # digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            # digitB = ord(b[i]) - ord('0') if i < len(b) else 0

            # calculate sum for current index 
            total = digitA + digitB + carry

            # get value to insert at current location
            char = total % 2

            # append char to result
            res += str(char)

            # get value to become carry for next iteration
            carry = total // 2

        # if carry has a value at the end, append to result
        if carry:
            res += str(carry)
        
        # reverse result before returning
        return res[::-1]
