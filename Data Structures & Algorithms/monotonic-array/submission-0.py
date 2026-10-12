class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing=True
        decreasing=True
        slow=0
        fast=1

        while fast <= len(nums)-1:
            if nums[slow]<nums[fast]:
                decreasing=False
            elif nums[slow]>nums[fast]:
                increasing=False

            slow+=1
            fast+=1
        
        return increasing or decreasing