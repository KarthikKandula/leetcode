class Solution:
    """
    we can solve the problem using sliding window & frequency hashmaps
        the twist with this problem is that
            we need to decrement left pointer for each iteration, to maintain constant window length
            update left pointer frequency in hashmap

            if at any point the frequencies match, add that index to result array
        return result array in end
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # create hashmaps for tracking values & frequencies
        countS, countP = {}, {}

        # for for each char in string p
        for i in range(len(p)):
            # increment count for character in P hashmap
            countP[p[i]] = countP.get(p[i], 0) + 1
            # incrment count for char in S hashmap
            countS[s[i]] = countS.get(s[i], 0) + 1

        # create a result array
        res = []

        # if arrays match at start, means 0th position has an anagram
        if countP == countS:
            res.append(0) # append 0 to result

        l = 0 # create left pointer

        # loop thru the string with right pointer
        for r in range(len(p), len(s)):
            # increment count for current variable in s hashmap
            countS[s[r]] = countS.get(s[r], 0) + 1
            countS[s[l]] -= 1 # decrement l pointer count

            # if l pointer's count is 0
            if countS[s[l]] == 0:
                countS.pop(s[l]) # pop the value from hashmap

            # increment l pointer
            l += 1

            # check if current hashmaps are similar
            if countP == countS:
                res.append(l) # if they are same, append l pointer to result

        # return result array
        return res
