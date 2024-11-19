class Solution:
    """
    we can treat this as a recursive decision-making problem
        the goal is to count the number of ways to decode a string of digits
        each digit or pair of digits can map to a letter (e.g., '1' -> 'A', '12' -> 'L')
        invalid digits (e.g., '0') or invalid pairs are excluded from valid paths

    create a helper function `dfs` to calculate the number of decoding paths starting at index `i`
        input is the current index (i) in the string
        define base cases:
            if index equals the length of the string (i == len(s)), return 1 since a valid decoding is complete
            if the current character is '0', return 0 because '0' cannot be decoded
        make recursive calls to calculate the decoding paths:
            add the result of decoding one digit (move to i + 1)
            add the result of decoding two digits if the pair is valid (e.g., 10 <= s[i:i+2] <= 26, move to i + 2)
        return the sum of these results for the current index

    start the recursion at index 0 and return the total number of decoding paths
        handle both single-digit and two-digit decoding paths for the entire string
        the base case ensures the recursion terminates when the string is fully decoded or an invalid state is reached
    """
    def numDecodings(self, s: str) -> int:
        
        # define cache
        cache = [-1] * len(s)

        # create helper function
        def dfs(i):
            # if i equal to length of s, we've found a possible path
            if i == len(s):
                return 1 # return 1 
            if s[i] == '0': # if current char is 0, it's not a valid value
                return 0 # return 0
            if cache[i] != -1:
                return cache[i]
            
            # make call for next digit
            res = dfs(i + 1)

            # check if we can make call for next 2 digits
            # check if it's in bounds between 10 - 26
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                res += dfs(i + 2) # recursive call to i + 2 i.e, including two digits & append to result
            
            cache[i] = res

            # return result
            return cache[i]

        # initial function call
        return dfs(0)


