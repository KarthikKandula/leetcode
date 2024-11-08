class Solution:
    """
    we can treat this problem as a graph traversal problem
        we can create a graph for every prereq given in the problem
        the goal is to make sure we can take every possible course by satisfying each prereq
        an added functionality is to return the order in which courses should be taken
            to account for this, we add to an output list whenever a course is satisfied 
            and record that course in a seperate set to make sure no other dfs path adds it to output

    create a hashmap with every course & populate the prereq's for each course
    create a set to take note of visited courses already -- helps in detecting cycles
    create a set to take note of prereq's satisfied courses already added to output
        helps not to add duplciate courses to output

    create a helper function to implement recursively
        input is a course
        if course is in visited
            return False
        if course is in prereq's satisfied set 
            return True
        
        if reaches this point, it means this is a new course we're visiting & should be validated
        add course to visited
        loop thru all prereq's this course has & recusively call each course
            if any course returns false, return false for entire function
        
        if reaches this point, it means no course returned false
        remove course from visited -- freeing up for other recursive paths
        add course to prereq's satisfied set, since all prereq'a are resolved
        add course to output list, since as of this point this course can be taken
        return True

    loop thru each course & recusively call for each call
        if any course returns false, return false for entire function
    
    in the end, return output list if we've not returned false anywhere else
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a hashmap to save courses & their respective prerequisites
        preReqMap = {i:[] for i in range(numCourses)} # Create as many empty arrays as numCourses

        # Loop thorugh input prerequisites - to populate hashmap
        for a, b in prerequisites:
            preReqMap[a].append(b)

        # create list to store output
        output = []

        # Create a set to track visited courses along a particular path
        visited = set()

        # Create a set to track courses that have added to output aka prereq's satisfied -- so not to add them again
        preReqSatisfied = set()

        # helper function to implement recursively to check prerequisites
        def dfs(course):
            # If input course is already in visitSet, it means there is a loop
            if course in visited:
                return False # Return False, since this is not possible
            # If input course is already in preReqSatisfied set, it means this course is already added to output
            if course in preReqSatisfied:
                return True
            
            # If program gets to this point, this course has not been visited & there are prereqs
            # Add this course to visitSet - for current path
            visited.add(course)

            # Loop through prereq's for this course to make recursive calls
            for eachPreReq in preReqMap[course]:
                # If the response is False for any requirements
                if not dfs(eachPreReq):
                    return False # return False, since it's not possible
                # If response is True prereqs are possible - continue for other courses
            
            # cleanup visited to not impact other dfs paths
            visited.remove(course)

            # if reaches this point, it means this course can be done
            # either doesn't have any prereq's or they have been resolved
            preReqSatisfied.add(course) # add to preReqSatisfied set -- to record so no other path's add to output
            output.append(course) # append to output, as of this point this course can be taken

            # return True, since this course is possible 
            return True
        
        # loop thru each course to call function
        # Call the function for every course in numCourses range, to account for unconnected graphs
        for course in range(numCourses):
            # If response for any course is False, fail entire thing
            if not dfs(course):
                return []
        
        # return output
        return output