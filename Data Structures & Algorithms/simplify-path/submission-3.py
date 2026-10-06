import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path.split("/"))
        bad_format=["",".",".."]
        string_stack=[]
        for string in path.split("/"):
            if string==".." and string_stack:
                string_stack.pop()
            elif string not in bad_format:
                string_stack.append(string)
        return "/"+"/".join(string_stack)


            
            
