class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited=[]
        sub_list=[]
        def subSetHelper(sublist,index):
            nonlocal nums
            #base case
            if index==len(nums):
                return []
            
            #recursive case
            sublist.append(nums[index]) 
            visited.append(sublist.copy())
            # keep
            subSetHelper(sublist,index+1)
            #Do not keep
            sublist.pop()
            subSetHelper(sublist,index+1)
        
        subSetHelper([],0)
        visited.append([])
        return visited
            
