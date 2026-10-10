class Solution:
    def isPalindrome(self, s: str) -> bool:
        def cleaner(s):
            final=[]
            for char in s:
                if char.isalnum():
                    final.append(char.lower())
            return "".join(final)

        def palinDromeHelper(s,l,r):
            if l>=r:
                return True
            if s[l]==s[r]:
                return palinDromeHelper(s,l+1,r-1)
            else:
                return False

        
        new_string=cleaner(s)
        return (palinDromeHelper(new_string,0,len(new_string)-1))