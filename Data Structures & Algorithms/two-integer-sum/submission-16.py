class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums={}
        for i in range(len(nums)):
            if target-nums[i] in seen_nums:
                return[seen_nums[target-nums[i]],i]
            seen_nums[nums[i]]=i

        