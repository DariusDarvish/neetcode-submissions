class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_stack={'[','{','('}
        closed_stack={']','}',')'}
        final_pair={'[]','()','{}'}
        for x in s:
            if x in open_stack:
                stack.append(x)
            elif x in closed_stack and stack:
                open_bracket=stack[-1]
                check_string=open_bracket+x
                if check_string in final_pair:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return True if not stack else False
