class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            midpoint=int((low+high)/2)
            if nums[midpoint]==target:
                return midpoint
            elif nums[midpoint]<target:
                low+=1
            else:
                high-=1
        return -1