class FileSystem:

    def __init__(self):
        # create hashmap to simulate file structure
        self.directory = {}

    def ls(self, path: str) -> List[str]:
        # split input path along / -- to get individual directories
        dirs = path.split('/')

        curr = self.directory # create pointer for directory -- easier to perform operations

        # if path isn't home
        if path != '/':
            # loop for each directory from input path
            for eachDir in dirs[1:]:
                # if a directory doesn't exist, return empty list
                if eachDir not in curr:
                    return []
                # if the directory is a file type i.e a list in our structure
                if type(curr[eachDir]) == list:
                    return [eachDir] # return a list with just that file name 
                
                # assign current directory as curr for next iteration
                curr = curr[eachDir]

        # create result variable
        res = []

        # loop for each directory in curr
        for eachDir in curr:
            # append result to directory
            res.append(eachDir)

        # return sorted list of values
        return sorted(res)

    def mkdir(self, path: str) -> None:
        # split input path along / -- to get individual directories
        dirs = path.split('/')

        curr = self.directory # create pointer for directory -- easier to perform operations

        # loop for each directory from input path
        for eachDir in dirs[1:]:
            # if a directory doesn't exist, create directory
            if eachDir not in curr:
                curr[eachDir] = {} # create new hashmap as a new directory
            
            # assign current directory as curr for next iteration
            curr = curr[eachDir]

    def addContentToFile(self, filePath: str, content: str) -> None:
        # split input path along / -- to get individual directories
        dirs = filePath.split('/')

        # extract file name from input, last value in filePath
        file = dirs[-1]

        curr = self.directory # create pointer for directory -- easier to perform operations

        # loop for each directory from input path, skip last dir since it's a file name
        for eachDir in dirs[1:-1]:
            # if a directory doesn't exist, create directory
            if eachDir not in curr:
                curr[eachDir] = {} # create new hashmap as a new directory
            
            # assign current directory as curr for next iteration
            curr = curr[eachDir]
        
        # if file doesn't exist in final directory
        if file not in curr:
            curr[file] = [] # create the file, as a list in our structure
        
        # append content to the file list
        curr[file].append(content)

    def readContentFromFile(self, filePath: str) -> str:
        # split input path along / -- to get individual directories
        dirs = filePath.split('/')

        # extract file name from input, last value in filePath
        file = dirs[-1]

        curr = self.directory # create pointer for directory -- easier to perform operations

        # loop for each directory from input path, skip last dir since it's a file name
        for eachDir in dirs[1:-1]:
            # assign current directory as curr for next iteration
            curr = curr[eachDir]
        
        # return values combined from the list as a string
        return "".join(curr[file])


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)