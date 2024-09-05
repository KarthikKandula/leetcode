class Solution:
    """
    solution using hashmaps
        one hashmap

        loop thru s & add the count of each value into the hashmap 
        loop thru t & subtract the count of each value into the hashmap 

        if any value in hashmapS not equal to 0
            return false
        else
            return true
    """
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if length of s & t is equal
        if len(s) != len(t):
            return False # If not, return False - since length has to be equal for strings to be anagrams

        hashmapS={}

        # 
        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)

        for i in range(len(t)):
            hashmapS[t[i]] = hashmapS.get(t[i], 0) - 1
            # if t[i] not in hashmapS or hashmapS[t[i]] == 0:
            #     return False
            # else:
            #     hashmapS[t[i]] = hashmapS.get(t[i], 0) - 1

        for x in hashmapS:
            if hashmapS[x] != 0:
                return False
        
        return True

    """
    solution using hashmaps
        two hashmaps
            each for s & t

        loop thru s & add the count of each value into s hashmap 
        loop thru t & add the count of each value into t hashmap 

        compare values in hashmapS & hashmapT
            if any value don't match
                return false
            else
                return true

    """
    # def isAnagram(self, s: str, t: str) -> bool:
    #     # Check if length of s & t is equal
    #     if len(s) != len(t):
    #         return False # If not, return False - since length has to be equal for strings to be anagrams

    #     hashmapS, hashmapT = {}, {}

    #     # 
    #     for i in range(len(s)):
    #         hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
    #         hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

    #     print(hashmapS, hashmapT)

    #     for x in hashmapS:
    #         # if x not in hashmapT or hashmapS[x] != hashmapT[x]:
    #         #     return False
    #         if hashmapS[x] != hashmapT.get(x,0):
    #             return False
        
    #     return True

    """
    My solution

    get list of all chars in s using list func
        loop thru t & remove each value
        if any value not in charList (from t) -> return false

        at the end compare if length of charList is 0
            if length is 0
                return true
            else
                return false
    """
    # def isAnagram(self, s: str, t: str) -> bool:
    #     # Check if length of s & t is equal
    #     if len(s) != len(t):
    #         return False # If not, return False - since length has to be equal for strings to be anagrams

    #     charList = list(s)

    #     for i in t:
    #         if i in charList:
    #             charList.remove(i)
    #         else:
    #             return False
        
    #     return True if len(charList) == 0 else False