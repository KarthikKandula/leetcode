class Solution:
    """
    we can treat this problem as a graph traversal problem
        we can create a graph for every prereq given in the problem
        the goal is to make sure we can take every possible course by satisfying each prereq
        
    create a hashmap with every course & populate the prereq's for each course
    create a set to take note of visited courses already -- helps in detecting cycles

    create a helper function to implement recursively
        input is a course
        if course is in visited
            return False
        if course has no prereq's in hashmap
            return True
        
        if reaches this point, it means this is a new course we're visiting & should be validated
        add course to visited
        loop thru all prereq's this course has & recusively call each course
            if any course returns false, return false for entire function
        
        if reaches this point, it means no course returned false
        remove prereq's for this course, since they're all cleared
        remove course from visited -- freeing up for other recursive paths
        return True

    loop thru each course & recusively call for each call
        if any course returns false, return false for entire function
    
    in the end, return true if we've not returned false anywhere else
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a hashmap to save courses & their respective prerequisites
        preReqMap = {x:[] for x in range(numCourses)} # Create as many empty arrays as numCourses
        visitSet = set() # Create a set to track visited courses along a particular path

        # Loop thorugh input prerequisites - to populate hashmap
        for crs, pre in prerequisites:
            preReqMap[crs].append(pre)
        
        # Recursive function to check prerequisites
        def checkPrereq(course):
            # If input course is already in visitSet, it means there is a loop
            if course in visitSet:
                return False # Return False, since this is not possible
            # If no prerequisites exists for this course in hashmap
            if preReqMap[course] == []:
                return True # return True, since this can be done
            
            # If program gets to this point, this course has not been visited & there are prereqs
            # Add this course to visitSet
            visitSet.add(course)

            # Loop through prereq'a for this course from the hashmap
            for req in preReqMap[course]:
                # If the response is False for any requirements
                if not checkPrereq(req): return False # return False, since it's not possible
                # If response is True prereqs are possible

            # If all prerequisites are satisfied, we can remove this course from visitSet
            visitSet.remove(course)
            # Empty this course's prereqs in hashmap, since all prereqs are satisfied 
            preReqMap[course] = []

            # return True since its possible 
            return True
        
        # Call the function for every course in numCourses range, to check for un connected graphs
        for crs in range(numCourses):
            # If response for any course is False, fail entire thing
            if not checkPrereq(crs): return False

        return True

