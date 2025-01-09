class Solution:
    def isPrefixAndSuffix(self, str1, str2) -> bool:
        len1 = len(str1)
        len2 = len(str2)
        
        if len1 > len2:
            return False
        
        return str2[:len1] == str1 and str2[-len1:] == str1

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res
