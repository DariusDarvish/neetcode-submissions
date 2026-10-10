class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_count=0
        current_count=0
        for num in nums:
            if num ==1:
                current_count+=1
            else:
                current_count=0
            longest_count=max(longest_count,current_count)
        return longest_count
    
