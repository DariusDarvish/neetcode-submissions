class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_characters={}
        current_count=0
        biggest_count=0
        left=0
        right=len(s)-1
        # if(len(s)==1):
        #     return 1
        while(left<=right):
            new_index=left
            if s[left] not in seen_characters:
                current_count+=1
                seen_characters[s[left]]=new_index
                left+=1
            elif s[left] in seen_characters:
                current_count=0
                left=seen_characters[s[left]]+1
                seen_characters={}
           
            biggest_count=max(biggest_count,current_count)
        return biggest_count
            
        