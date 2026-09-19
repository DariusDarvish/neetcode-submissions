class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited=[]
        sublist=[]
        def subSetHelper(index):
            nonlocal nums
            #base case
            if index>=len(nums):
                visited.append(sublist.copy())
                return
            
            #recursive case
            sublist.append(nums[index]) 
            # keep
            subSetHelper(index+1)
            #Do not keep
            sublist.pop()
            subSetHelper(index+1)
        
        subSetHelper(0)
        return visited
            
