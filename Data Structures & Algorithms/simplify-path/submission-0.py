class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        /neetcode/practice/courses
        /
        /_home/a/b

        algo:
            path.split('/') -> list of all the words
            iterate through list, if elem == '', continue
            if elem == ., add to stack
            if elem == .., pop from stack

            stack holds elements of the path that we want
            res = "/".join(stack)
        '''
        path_list = path.split('/')
        stack = []

        for elem in path_list:
            if elem == '' or elem == '.':
                continue
            elif elem == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(elem)

        res = "/".join(stack) 
        res = "/" + res
        return res
                        