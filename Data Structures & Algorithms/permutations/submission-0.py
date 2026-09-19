class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited=[]

        def backTracking(nums,subset):
            nonlocal visited
            if len(nums)==len(subset):
                visited.append(subset.copy())
                return

            for x in nums:
                if x not in subset:
                    subset.append(x)
                    backTracking(nums,subset)
                    subset.pop()
            
            return visited
        
        final_output=backTracking(nums,[])
        return final_output