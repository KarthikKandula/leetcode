class Solution:
    """
    iterative solution
    """
    def countAndSay(self, n: int) -> str:
        # create base case result
        res = '1'

        # loop for n iterations starting from 2 -- since we have 1st base case
        for i in range(2, n + 1):
            # to record num & chars
            num, char = 0, ""
            tempRes = "" # to construct res for this iteration

            # loop for every char in previous result
            for c in res:
                # if current char isn't same as last char & num isn't 0 -- to skip first iteration
                if char != c and num != 0:
                    # process current vals
                    # add current num & char to result
                    tempRes += str(num)+char

                    # reset num & char to base state
                    num = 0
                    char = ""

                # add curr char to variables
                num += 1
                char = c
            
            # final processing after loop ends
            if num != 0:
                tempRes += str(num)+char
            
            # assign result built this loop to result -- will be processed next loop
            res = tempRes
        
        # return result
        return res


    """
    recursive solution
    """
    def countAndSay(self, n: int) -> str:
        # base conditions
        # if n is 1, return base value
        if n == 1:
            return "1"
        
        # get rle for n-1 value
        rle = self.countAndSay(n - 1)

        # base result
        res = ""

        # process n-1 rle
        num, char = 0, ""
        for c in rle:
            # if current char isn't same as last char & num isn't 0 -- to skip first iteration
            if char != c and num != 0:
                # process current vals
                # add current num & char to result
                res += str(num)+char

                # reset num & char to base state
                num = 0
                char = ""

            # add curr char to variables
            num += 1
            char = c
        
        # final processing after loop ends
        if num != 0:
            res += str(num)+char

        # return final result 
        return res
