class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1

        while(low<=high):
            mid=high-low//2
            print(nums[mid])
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                low +=1
            else:
                high-=1
        return -1

        

        
