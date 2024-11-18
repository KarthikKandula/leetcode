class Solution:
    """
    we'd have to compare for palindromes for each substring in the given input
        instead of comparing from the outsides of a string & coming inwards
        let's put a simple twist
            let's check from inside -> out
            for every character, see how big of a palindrome can be formed by going out
            keep updating final result & result length variables as you go
            this way, the num of comparision are reduced

    the only downside of this approach is that
        We have to take two different approaches for this
            1. To check for odd length palindromes
                - We assign l, r = i 
            2. To check for even length palindromes
                - We assign l, r = i, i+1
    """
    def longestPalindrome(self, s: str) -> str:
        # Create variables for result & result length
        res, resLen = "", 0

        # Loop through the length of input s for odd num palidromes
        for i in range(len(s)):
            l, r = i, i # Left & right pointers

            # loop while l & r are in bounds & s[l] = s[r]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If above condition is true, it means it's a palindrome
                # check if current palindrome is longer
                if (r - l + 1) > resLen:
                    # update length 
                    resLen = (r - l + 1)
                    # update palindrome substring
                    res = s[l:r+1]
                l -= 1 # Decrement l
                r += 1 # Increment r

        # Loop through the length of input s for even num palidromes
        for i in range(len(s)):
            l, r = i, i + 1 # Left & right pointers

            # loop while l & r are in bounds & s[l] = s[r]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If above condition is true, it means it's a palindrome
                # check if current palindrome is longer
                if (r - l + 1) > resLen:
                    # update length 
                    resLen = (r - l + 1)
                    # update palindrome substring
                    res = s[l:r+1]
                l -= 1 # Decrement l
                r += 1 # Increment r

        # return res
        return res

