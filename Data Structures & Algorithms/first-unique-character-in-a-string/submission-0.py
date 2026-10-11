from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        default_dict = defaultdict(list) 
        lowest_index = [] 
        for i in range(len(s)):
            default_dict[s[i]].append(i)
        for key,val in default_dict.items():
            if len(val)==1:
                lowest_index.append(val[0])
        if len(lowest_index)==0:
            return -1
        return min(lowest_index)

        