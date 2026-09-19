class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        flat_list = [item for row in matrix for item in row]
        right=len(flat_list) - 1
        while(left<=right):
            middle=(left+right)//2
            if(target<flat_list[middle]):
                right=middle-1
            elif(target>flat_list[middle]):
                left=middle+1
            else:
                return True
        return False