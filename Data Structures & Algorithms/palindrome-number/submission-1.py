class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        def palindromeHelper(string,left,right):
            if left>=right:
                return True
            if string[left]==string[right]:
                left+=1
                right-=1
                return palindromeHelper(string,left,right)        
            else:
                return False
        

        return palindromeHelper(string,0,len(string)-1)