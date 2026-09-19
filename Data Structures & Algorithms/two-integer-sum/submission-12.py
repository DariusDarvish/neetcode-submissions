class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set={}
        for i in range(len(nums)):
            if nums[i] not in hash_set:
                hash_set[nums[i]]=[i]
            else:
                hash_set[nums[i]].append(i)
        
        for i in range(len(nums)):
            if target-nums[i] in hash_set and len(hash_set[target-nums[i]])==1:
                if i!=hash_set[target-nums[i]][0]:
                    return [i,hash_set[target-nums[i]][0]]
            elif target-nums[i] in hash_set and len(hash_set[target-nums[i]])>1:
                return [i,hash_set[target-nums[i]][1]]

        
        