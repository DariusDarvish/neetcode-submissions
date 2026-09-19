class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Tracks the last index of each character
        max_length = 0
        left = 0       # Left boundary of the sliding window
        
        for right in range(len(s)):
            # If the character is a duplicate and is inside our current window
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1 # Move the left pointer past the last duplicate
            
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length