class Solution:
    def isPalindrome(self, x: int) -> bool:
        # acc to prblm statement, if x is negative, never will be palindrome
        if x < 0:
            return False
        
        # create varibles for new number & duplicate of input
        new = 0
        dup = x

        # loop while input is greater than 0
        while x > 0:
            # get remainder
            temp = x % 10

            # multiply to generate new number
            new = (new * 10) + temp

            # divide current number by 10 to remove last digit
            x //= 10
        
        # return True if new generated number is same as input
        return True if dup == new else False
