class Solution:
    def romanToInt(self, s: str) -> int:
        # create hashmap to store roman values
        vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        prev = 0 # variable to track previous value
        total = 0 # to store total value

        # loop thru input in reverse order -- makes it easier for 4 & 9 ops
        for i in range(len(s) - 1, -1, -1):
            # if previous value is greater than current val
            if prev > vals[s[i]]:
                # reduce current val from total
                total -= vals[s[i]]
                continue # skip further logic
            
            # if reaches this point, it's a regular ops
            # add current value to total
            total += vals[s[i]]
            prev = vals[s[i]] # assign current value as prev for next iteration

        # return answer
        return total
