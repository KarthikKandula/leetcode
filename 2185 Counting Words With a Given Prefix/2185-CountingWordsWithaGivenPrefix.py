class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref) # get length of pref in a variable

        # variable to count
        count = 0

        # loop thru each word in input words
        for word in words:
            # check if first n words are same as pref
            if word[:n] == pref:
                count += 1 # increment count

        # return count
        return count
