class Solution:
    """
    One Hashmaps approach
        get the count of each char from magazine
        now, go thru each char in ransomNote 
            decrement each char as seen from magazine hashmap
            if any letter is 0 before decrementing
            it means, there are not enough letters in magazine
                return False
        if false condition isn't hit inside, return True
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # get counts of letters in magazine
        letters = Counter(magazine)

        # loop thru each char in ransom note
        for c in ransomNote:
            # if count in hashmap for this letter is 0
            if letters[c] <= 0:
                return False # not enough letters, return False
            
            # decrement 1 from letters, if above condition isn't hit
            letters[c] -= 1
        
        # return true, if above false condition isn't hit
        return True

    """
    Two Hashmaps approach
        get counts of two inputs
        now go thru the chars & counts from ransom note
            check if the count from magazine matches or exceeds the value
            if it doesn't, return False
        if false condition isn't hit, return True
    """
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     # get counts of ransom note
    #     c1 = Counter(ransomNote)
    #     # get counts of magazine
    #     c2 = Counter(magazine)

    #     # loop for each char, count from ransom note
    #     for char, count in c1.items():
    #         # check if this char exists in c2 & the count is sufficient
    #         if char not in c2 or c1[char] > c2[char]:
    #             return False # if not, not enough letters, return false
        
    #     # return true, if above false conditions isn't hit
    #     return True
