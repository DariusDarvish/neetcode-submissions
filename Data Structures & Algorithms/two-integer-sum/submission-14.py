class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map ={}
        for x in range(len(nums)):
            diff=target-nums[x]
            if diff in hash_map:
                return [hash_map[diff],x]
            hash_map[nums[x]]=x