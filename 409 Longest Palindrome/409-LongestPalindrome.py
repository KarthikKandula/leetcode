class Solution:
    def longestPalindrome(self, s: str) -> int:
        # get counts of each letter in input s
        count = Counter(s)

        # variable to count odd values
        oddCount = 0

        # variable to count result
        res = 0

        # loop thru each count value in hashmap
        for key, val in count.items():
            # res += (val - 1) if val % 2 else val
            
            # if count value is odd
            if val % 2:
                # increment odd count
                oddCount += 1
                # add val - 1 to result since we can use even no. of occurences in palindrome
                res += (val - 1)
            # if count value is even
            else:
                # add val to result since we can use all occurences in palindrome
                res += val

        # return result
        return res if oddCount == 0 else res + 1

