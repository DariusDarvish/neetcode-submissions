class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=len(s)-1
        left=0
        while(left<right):
            if(s[right].isalnum()==s[left].isalnum() and s[right].lower()==s[left].lower()):
                left+=1
                right-=1
            elif(s[right].isalnum()==False):
                right-=1
            elif(s[left].isalnum()==False):
                left+=1
            else:
                return False

           
        return True