class Solution:
    """
    the idea is to extract all the values in input one digit at a time,
    and insert them back in reverse order 1 digit at a time

    extracting values one digit at a time
        right shift n with each number until range i & then and with 1
        gives the right most value
    
    insert them back in reverse order
        create a result array with initial value 0
        take the right most value from above & or it with result array -- OR preserves all 1's already in result
        since we need to insert them in right order, left shit it by 31 - i (i is the location where to insert)

    essentially we're getting a location from right & insert it in the same location from left 
        so on opposite sides of the spectrum
    """
    def reverseBits(self, n: int) -> int:
        res = 0 # create variable to store result

        # loop for 32 bits -- every input is a 32 bit integer
        for i in range(32):
            # get value in ones place by right shifting n with i & anding with 1 -- gets the value in ones place
            digit = (n >> i) & 1

            # now place the extracted digit in reversed order -- left shift by 31 to get reverse order location
            res = res | (digit << (31 - i))

        # return result
        return res
