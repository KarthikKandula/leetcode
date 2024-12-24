class Solution:
    def simplifyPath(self, path: str) -> str:
        # create stack
        stack = []
        # split input path with /
        path = path.split('/')

        # loop thru each path param
        for each in path:
            # if stack is initialized & path param is ..
            if stack and each == '..':
                stack.pop() # pop from stack
            # if path param is anything other than the below 3
            elif each not in ['', '.', '..']:
                stack.append(each) # append to stack

        # return values in stack joined by a /
        return "/" + '/'.join(stack)
