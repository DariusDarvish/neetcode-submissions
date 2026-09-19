class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left=0
        right=len(cleaned_text)-1
        print(cleaned_text)
        while(left<=right):
            if cleaned_text[left] != cleaned_text[right]:
                return False
            left+=1
            right-=1
        return True
