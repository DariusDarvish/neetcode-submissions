class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            print('x is',x)
            if self.is_numeric_with_negatives(x):
                print("appending",x)
                stack.append(x)
            else:
                last=stack.pop()
                first=stack.pop()
                print("lets evaluate",first + x + last)
                new_value=int(eval(first + x + last))
                stack.append(str(new_value))
                print('appending to stack',new_value)
                print(stack)
        return int(stack[0])

    def is_numeric_with_negatives(self,text):
        return text.lstrip('-').isnumeric()