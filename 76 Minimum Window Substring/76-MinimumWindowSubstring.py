class Solution:
    """
        Use sliding window approach to solve the problem
            in a nutshell the problem is to find the smallest substring that has all letters from t in s, can also have other letters
            and the return value is the actual substring itself

        First, we get a count of every letter in t

        Loop thru string s - using your right pointer
            left & right pointers are in the same location
            have two variables have & need
                have - is the count of letters from t we currently have in our window in this iteration of s
                need - is the count of letters from t we're required to have
            As looping thru the input s string, increment have as you find variables in t - ignore for the other letters

            check if at any time have == need, 
                if they are it means in the current window we have all the letters from t
                but since our objective is to find the minimum substring, start removing letters from left pointer
                update the result length & start & end index of current window as you go
                and if at any point you eat into something in the have string, decrement accordingly

        loop thru the end of the string
            the final result length & start, end index of substring is in the result variables 
    """
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return "" # edge case to handle empty t string

        # Initialize two hashmaps to keep track of counts in two strings
        countT, countS = {}, {}

        # populate countT
        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        # Initialize variables for recording result & result length
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(countT) # create two variables to keep track of have (counts of s) & need (counts of t) 
        l = 0 # left pointer

        # loop thru input s, r is the right pointer here
        for r in range(len(s)):
            # populate countS in each iteration
            countS[s[r]] = 1 + countS.get(s[r], 0)

            # check if current right pointer value is part of countT & if this value's count match in countS & countT - basically checking if the count condition is satisfied for this value
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1 # increment have value
            
            # while have == need, try to decrement the substring as much as possible since we need minimum substring
            while have == need:
                # check if current length (r - l + 1) is less than result Length variable - since we want the minimum substring
                if (r - l + 1) < resLen:
                    res = [l, r] # update result start & end indexes
                    resLen = (r - l + 1) # update result length

                # decrease the count of current left pointer value in countS
                countS[s[l]] -= 1

                # check if current left pointer value is part of countT & if this value's count is less in countS - basically checking if we're eating into one of our have values
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1 # decrement have value if we just removed one of the required values

                l += 1 # increment left pointer

        # return sliced s string based out of result indexes we saved from above
        return s[res[0]:res[1]+1] if resLen < float("infinity") else ""

