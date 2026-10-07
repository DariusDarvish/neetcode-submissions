# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(left_side,right_side):
            left=0
            right=0
            final_list=[]
            while left<len(left_side) and right<len(right_side):
                left_op=left_side[left].key
                right_op=right_side[right].key
                if left_op<=right_op:
                    final_list.append(left_side[left])
                    left+=1
                else:
                    final_list.append(right_side[right])
                    right+=1
            if left<len(left_side):
                final_list=final_list+left_side[left:]
            if right<len(right_side):
                final_list=final_list+right_side[right:]
            return final_list


        if len(pairs)==1 or len(pairs)==0:
            return pairs

        midpoint=len(pairs)//2
        left=pairs[:midpoint]
        right=pairs[midpoint:]
        left_side=self.mergeSort(left)
        right_side=self.mergeSort(right)
        return merge(left_side,right_side)

