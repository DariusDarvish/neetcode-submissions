class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if self.is_numeric_with_negatives(x):
                stack.append(x)
            else:
                last=stack.pop()
                first=stack.pop()
                new_value=int(eval(first + x + last))
                stack.append(str(new_value))
        return int(stack[0])

    def is_numeric_with_negatives(self,text):
        return text.lstrip('-').isnumeric()