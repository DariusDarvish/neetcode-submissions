class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        int_dict={}
        for integers in nums:
            if integers not in int_dict:
                int_dict[integers]=0
            int_dict[integers]+=1
            if int_dict[integers]>1:
                return True
        return False