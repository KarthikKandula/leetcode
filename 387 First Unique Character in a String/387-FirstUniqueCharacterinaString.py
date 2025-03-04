class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hashmap to take note of counts of each char
        hashmap = {}

        # populate hashmap with char freq
        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        # loop thru input again, to find the first non-repeating char
        for i, c in enumerate(s):
            # if count of this char is 1, only occurring once
            if hashmap[c] == 1:
                return i # return i
        
        # if return isn't triggered inside
        return -1
