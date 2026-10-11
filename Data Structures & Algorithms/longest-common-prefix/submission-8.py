class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string=strs[0]
        current_prefix=""
        for i in range(len(first_string)):
            for string in strs:
                if i>len(string)-1 or first_string[i]!=string[i]:
                    return current_prefix
            current_prefix=current_prefix+first_string[i]
        return current_prefix