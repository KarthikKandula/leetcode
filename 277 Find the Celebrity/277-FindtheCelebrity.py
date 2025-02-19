# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    """
    Optimal solution

    this is a classic graph traversal and elimination problem
        this focuses on reducing search space efficiency
        the nodes are directed i.e directed edges
        first we eliminate non celebrities in one pass
            we check all nodes one by one with a possible celebrity candidate
            if any candidate knows any node
                it's not a celebrity
                the new node becomes a celebrity candidate now
            doing this until end, leaves us with one celebrity candidate
        now we confirm if this candidate is indeed a celebrity
            to be a celeb, this candidate shouldn't know anyone
            and everyone else should know this candidate
            if at anytime this condition is breached
            return there is no celeb
    """
    def findCelebrity(self, n: int) -> int:
        # initialize a possible candidate
        candidate = 0

        # loop thru all possible nodes & check if they know
        for i in range(n):
            if knows(candidate, i):
                # replace candidate
                candidate = i
        
        # loop for all possible nodes
        for j in range(n):
            # if same person, skip 
            if candidate == j: continue
            
            # check if this candidate knows j or j knows candidate
            if knows(candidate, j) or not knows(j, candidate):
                # if any of the condition matches, return -1, no celebrity exists
                return -1
        
        # return candidate
        return candidate

    """
    My solution

    this solution tries to find a celeb by trying to check all possible combinations first and eliminating them early
        out of the remaining nodes, we then try to check with all other nodes 
        if they know the celeb candidate and the celeb candidate knows no one.
    """
    # def findCelebrity(self, n: int) -> int:
    #     removed = set()

    #     # eliminate node values
    #     for i in range(n):
    #         if i in removed:
    #             continue

    #         for j in range(n):
    #             if i == j or j in removed:
    #                 continue
    
    #             temp = knows(i, j)

    #             # if i doesn't know j -- j not a celeb
    #             if temp == 0:
    #                 removed.add(j)
    #             # if i knows j -- i not a celeb
    #             elif temp == 1:
    #                 removed.add(i)
        
    #     print(removed)

    #     res = -1
    #     for i in range(n):
    #         if i in removed:
    #             continue
            
    #         res = i

    #         for j in range(n):
    #             if i == j:
    #                 continue

    #             if knows(i, j) or not knows(j, i):
    #                 return -1

    #             # temp = knows(i, j)

    #             # if temp == 1:
    #             #     return -1

    #     return res

