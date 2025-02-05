class Solution:
    """
    to solve this problem without using any operators
        we need to use bitwise operators to solve this
        first, determine if there is a carry to be moved 
            carry can be extracted by using &
        second, perform additions without any carry
            this can be done using bitwise XOR ^
        next, move carry to the next location
            by shifting it 1 place to the left
            using << operator
        once carry becomes 0, we have our sum in the variable using to perform additions 
    """
    def sum(self, num1: int, num2: int) -> int:
        mask = 0xFFFFFFFF  # 32 bits of all 1s
        max_int = 0x7FFFFFFF  # Largest positive 32-bit integer: 011...1 (31 bits of 1)

        # loop while num2 is not equal to 0
        while num2 != 0:
            # num1 & num2 identifies the positions where both bits are 1 (these positions will generate a carry)
            # << 1 shifts the carry to the next higher bit (where it should be added in the next iteration)
            carry = (num1 & num2) << 1

            # num1 ^ num2 performs addition without carry
            # Applying & mask ensures the result is limited to 32 bits
            num1 = (num1 ^ num2) & mask

            # num2 now becomes the carry (masked to ensure 32 bits)
            num2 = carry & mask

        # if num1 is less than or equal to max_int, return as is
        # if num1 is greater than max_int, the result is negative in two’s complement representation, convert to negative
        # num1 ^ mask - Flips the 32 bits of num1
        # ~ - Negates the flipped bits, effectively converting it to its negative representation
        return num1 if num1 <= max_int else ~(num1 ^ mask)

