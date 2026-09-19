class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_dict={}
        for index in range(len(nums)):
            if nums[index] not in int_dict:
                int_dict[nums[index]]=[]
            int_dict[nums[index]].append(index)
        for key,val in int_dict.items():

            if target-key in int_dict:
                if len(int_dict.get(target-key))>1:
                    return[val[0],val[1]]
                if val[0] != int_dict.get(target-key)[0]:
                    return[val[0],int_dict.get(target-key)[0]]