class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def climbHelper(total):
            if total==0 or total==1:
                return 1
            if total in memo:
                return memo[total]
            memo[total]=climbHelper(total-2)+climbHelper(total-1)
            return memo[total]

        return climbHelper(n)
        
            