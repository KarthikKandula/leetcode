class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # if length of string is less than k, it's not possible to form k palindrome strings 
        if len(s) < k:
            return False

        # get count of values in input s
        count = Counter(s)

        # variable to track odd counts
        oddCounts = 0

        # loop for each value in count hashmap to get odd counts
        for key, v in count.items():
            if v % 2:
                oddCounts += 1

        # return True if oddcounts are less than k & false if not
        return True if oddCounts <= k else False
