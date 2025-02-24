class Solution:
    """
    Optimal solution
    same as my solution but a bit better
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # array to store trusted values
        trusted = [0] * n

        # loop thru input
        for a, b in trust:
            # -1 for person if they trust someone
            trusted[a - 1] -= 1
            # +1 if another person trusts them
            trusted[b - 1] += 1
        
        # loop thru input 
        for i in range(n):
            # if anyone has a value of n - 1, it means everyone trusts them but they trust no one
            if trusted[i] == n - 1:
                return i + 1
        
        # if return isn't hit from above
        return -1


    """
    My solution
    """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustees = [0] * n # no. of people trust this person
        trusted = [0] * n # no. of people this person trusts

        # loop thru input to populate above arrays
        for a, b in trust:
            trusted[a - 1] += 1
            trustees[b - 1] += 1
        
        # loop thru no. of nodes
        for i in range(n):
            # check if the no. of people trusts this person in n - 1 i.e all people trusts
            # check if no. of people this person trusts is 0
            if trustees[i] == n - 1 and trusted[i] == 0:
                return i + 1 # if yes, return
        
        #if return not hit above, return -1
        return -1

