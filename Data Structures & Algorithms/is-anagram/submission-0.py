class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=self.createDict(s)
        s2=self.createDict(t)
        if s1==s2:
            return True
        else:
            return False

    def createDict(self,s:str) -> dict:
        char_dict={}
        for char in s:
            if char not in char_dict:
                char_dict[char]=0
            char_dict[char]+=1
        return char_dict