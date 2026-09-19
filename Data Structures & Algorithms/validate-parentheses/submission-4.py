class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_stack={'[','{','('}
        closed_stack={']','}',')'}
        final_pair={'[]','()','{}'}
        for x in s:
            if x in open_stack:
                stack.append(x)
            elif x in closed_stack:
                if len(stack)==0:
                    return False
                open_bracket=stack[-1]
                check_string=open_bracket+x
                if check_string in final_pair:
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        return True
