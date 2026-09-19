# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(left,right):
            l=0
            r=0
            new_output=[]
            while l<len(left) and r<len(right):
                if left[l].key <= right[r].key:
                    new_output.append(left[l])
                    l+=1
                else:
                    new_output.append(right[r])
                    r+=1
            if l<len(left):
                new_output+=left[l:]
            if r<len(right):
                new_output+=right[r:]
            return new_output
        
        if len(pairs)==1 or len(pairs)==0:
            return pairs
        midpoint=len(pairs)//2
        left_side=self.mergeSort(pairs[:midpoint])
        right_side=self.mergeSort(pairs[midpoint:])
        sorted_pair=merge(left_side,right_side)
        return sorted_pair

