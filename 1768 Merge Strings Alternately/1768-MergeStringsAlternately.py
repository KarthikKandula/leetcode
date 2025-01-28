class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # get lengths into variables for easy access
        n = len(word1)
        m = len(word2)

        res = "" # variable to store result in

        # get max length of inputs
        maxStr = max(n, m)
        
        # loop for the length of max string
        for i in range(maxStr):
            # if current index is less than length of word1, we can add it to result
            if i < n:
                res += word1[i]
            # if current index is less than length of word2, we can add it to result
            if i < m:
                res += word2[i]

        # alternate code to get the remaining chars from the longer string
        # if minStr < n:
        #     res += word1[minStr:]
        # if minStr < m:
        #     res += word2[minStr:]

        # return result
        return res
