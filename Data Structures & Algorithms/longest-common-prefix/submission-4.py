class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word=strs[0]
        longest_substring=''
        for i in range(len(first_word)):
            for s in strs:
                if i < len(s) and first_word[i]==s[i]:
                    continue
                else:
                    return longest_substring
            longest_substring+=first_word[i]
        return longest_substring
                

                
