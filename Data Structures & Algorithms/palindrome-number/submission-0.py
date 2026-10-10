class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        
        def palindromeHelper(string):
            if len(string) <=1:
                return True
            
            if string[0]==string[-1]:
                return palindromeHelper(string[1:-1])
            else:
                return False
        

        return palindromeHelper(string)