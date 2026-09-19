class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited=[]
        def dfs(subset,index):
            nonlocal nums

            #base case
            if index==len(nums):
                visited.append(subset)
                return

            dfs(subset+[nums[index]],index+1)
            dfs(subset,index+1)
        dfs([],0)
        return visited