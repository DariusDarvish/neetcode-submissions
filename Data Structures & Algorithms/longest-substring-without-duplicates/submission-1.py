class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_count=0
        seen_characters={}
        character_count=0
        while(character_count<len(s)):
            if(seen_characters.get(s[character_count])!=None):
                seen_characters={}
                character_count=0
                s=s[1:]
            else:
                seen_characters[s[character_count]]=True
                character_count+=1
                if(character_count>longest_count):
                    longest_count=character_count

        return longest_count

        


        


