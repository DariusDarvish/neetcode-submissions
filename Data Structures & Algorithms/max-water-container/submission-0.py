class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length=heights[0]
        width=0
        total=0
        head=0
        tail=len(heights)-1
        while(head<tail):
            length=min(heights[head],heights[tail])
            width=tail-head
            total=max(total,length*width)
            tail-=1
            if(tail==head):
                head+=1
                tail=len(heights)-1

        return total

