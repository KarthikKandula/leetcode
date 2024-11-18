class Solution:
    """
    we can treat this as a two-pointer expansion problem
        the goal is to count all palindromic substrings in the input string
        a substring is a palindrome if it reads the same forwards and backwards
        to count all palindromes, we explore around each character in the string as a potential center

    create a helper function `countPali` to count palindromes centered at a given pair of indices (l, r)
        input is the string `s`, and two pointers `l` and `r` representing the center
        while `l` and `r` are in bounds and the characters match, increment the result count
        move the left pointer leftward (l -= 1)
        move the right pointer rightward (r += 1)
        return the count of palindromes found for this center

    loop through each character in the string as a potential center for palindromes
        for each index `i`:
        perform two operations:
            count odd-length palindromes using `countPali` with the center at `i` (l = r = i)
            count even-length palindromes using `countPali` with the center between `i` and `i + 1` (l = i, r = i + 1)
        add the counts from both operations to the total result

    return the total result as the number of palindromic substrings in the input string
    """
    def countSubstrings(self, s: str) -> int:
        out = 0 # create a result variable

        # loop thru the length of input s
        for i in range(len(s)):
            # odd operation
            # left & right pointers 
            l, r = i, i
            out += self.countPali(s, l, r) # call function to count palindromes at this location & add to output variable
            
            # odd operation
            # left & right pointers, right pointer is for next index
            l, r = i, i + 1
            out += self.countPali(s, l, r) # call function to count palindromes at this location & add to output variable
        
        # return output
        return out

    # create a helper function to implement counting palindromes given string, left & right pointers
    def countPali(self, s, l, r) -> int:
        res = 0 # create a result variable

        # Loop through the length of input s for odd num palidromes
        for i in range(len(s)):

            # loop while l & r are in bounds & s[l] = s[r]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1 # increment result value by 1 -- since a palindrome has been found
                l -= 1 # Decrement l
                r += 1 # Increment r
        
        # return result
        return res


    # def countSubstrings(self, s: str) -> int:
    #     # Create variables for result & result length
    #     out = 0

    #     # Loop through the length of input s for odd num palidromes
    #     for i in range(len(s)):
    #         l, r = i, i # Left & right pointers

    #         # loop while l & r are in bounds & s[l] = s[r]
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             out += 1 # increment result value by 1 -- since a palindrome has been found
    #             l -= 1 # Decrement l
    #             r += 1 # Increment r

    #     # Loop through the length of input s for even num palidromes
    #     for i in range(len(s)):
    #         l, r = i, i + 1 # Left & right pointers

    #         # loop while l & r are in bounds & s[l] = s[r]
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             out += 1 # increment result value by 1 -- since a palindrome has been found
    #             l -= 1 # Decrement l
    #             r += 1 # Increment r

    #     # return res
    #     return out