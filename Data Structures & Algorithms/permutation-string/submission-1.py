from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=len(s1)
        s1_dict=Counter(s1)
        while(right<=len(s2)):
            s2_dict=Counter(s2[left:right])
            if s1_dict==s2_dict:
                return True
            left+=1
            right+=1
        return False


        