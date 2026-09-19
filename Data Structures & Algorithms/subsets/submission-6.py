class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited=[]
        def subSetHelper(sublist,index):
            nonlocal nums
            #base case
            if index>=len(nums):
                visited.append(sublist)
                return
            
            # #recursive case
            # we get clost to the end by adding one to index
            # we pass the current sublist 
            # keep
            subSetHelper(sublist+[nums[index]],index+1)
            #Do not keep
            subSetHelper(sublist,index+1)
        
        subSetHelper([],0)
        return visited
            
