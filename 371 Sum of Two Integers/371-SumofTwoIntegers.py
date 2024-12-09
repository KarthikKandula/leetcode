class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32 bits of all 1s
        max_int = 0x7FFFFFFF  # Largest positive 32-bit integer: 011...1 (31 bits of 1)

        # loop while b is not equal to 0
        while b != 0:
            # a & b identifies the positions where both bits are 1 (these positions will generate a carry)
            # << 1 shifts the carry to the next higher bit (where it should be added in the next iteration)
            carry = (a & b) << 1

            # a ^ b performs addition without carry
            # Applying & mask ensures the result is limited to 32 bits
            a = (a ^ b) & mask

            # b now becomes the carry (masked to ensure 32 bits)
            b = carry & mask

        # if a is less than or equal to max_int, return as is
        # if a is greater than max_int, the result is negative in two’s complement representation, convert to negative
        # a ^ mask - Flips the 32 bits of a
        # ~ - Negates the flipped bits, effectively converting it to its negative representation
        return a if a <= max_int else ~(a ^ mask)
