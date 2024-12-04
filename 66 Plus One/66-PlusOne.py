class Solution:
    """
    Optimal solution

    idea behind this solution is to use addition to our advantage
        if all we're doing is adding 1, it's added to the last digit 1st
        if there needs to be a carry then it's added to next digit
        we use this knowledge 
    
    loop thru the input in reverse order
        if a digit is less than 9, we can add 1 to that place & return result
            this by default works for any no. of 9's in the input
        if a digit is 9, that location should be made 0 & 1 to be added to next location
    
    one edge case to be taken note of is if the inputs are all 9's, in the end we return with 1 added to the front
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            # if this digit is less than 9
            if digits[i] < 9:
                # increment it
                digits[i] += 1
                # return it
                return digits
            
            # if value is not returned after 1st iteration, it means there is a carry
            # so mark current location as 0 & in the next iteration, 1 will be added to higher digit
            digits[i] = 0

        # if result is not returned above, input is all 9's, so add a 1 i.e carry before returning
        return [1] + digits

    """
    Own solution
    """
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     temp = 0

    #     for c in digits:
    #         temp *= 10
    #         temp += c

    #     return [int(digit) for digit in str(temp + 1)]