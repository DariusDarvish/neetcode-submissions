# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def merge(left,right):
            new_list=[]
            l=0
            r=0
            while(l<len(left) and r<len(right)):
                if(left[l].key<=right[r].key):
                    new_list.append(left[l])
                    l+=1
                else:
                    new_list.append(right[r])
                    r+=1
            if(l<len(left)):
                new_list+=left[l:]
            if(r<len(right)):
                new_list+=right[r:]
            return new_list

        if len(pairs)==1 or len(pairs)==0:
            return pairs
        mid=len(pairs)//2
        left=pairs[:mid]
        right=pairs[mid:]
        left_array=self.mergeSort(left)
        right_array=self.mergeSort(right)
        final_output=merge(left_array,right_array)
        return final_output
        