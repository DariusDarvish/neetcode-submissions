class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def palindromeChecker(string,left,right):
            if left>=right:
                return True
            elif string[left]==string[right]:
                return palindromeChecker(string,left+1,right-1)
            else:
                return False
        string=str(x)
        return palindromeChecker(string,0,len(string)-1)