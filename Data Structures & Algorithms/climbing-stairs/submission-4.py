class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def climb(count):
            if count==0 or count==1:
                return 1
            
            if count in memo:
                return memo[count]

            memo[count]=climb(count-2)+climb(count-1)
            return memo[count]

        return climb(n)    