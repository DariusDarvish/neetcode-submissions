# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # divide the array into two halves 
        # recusvely sort each
        # merge the two halves

        def mergeSortHelper(array):
            if len(array)<=1:
                return array
            mid_point=len(array)//2
            left_side=mergeSortHelper(array[:mid_point])
            right_side=mergeSortHelper(array[mid_point:])
            merged_list=merge(left_side,right_side)
            return merged_list

        def merge(left,right):
            l=0 #left side iteration
            r=0 #right side iteration
            final_output=[]
            while l<=len(left)-1 and r<=len(right)-1:
                if(left[l].key<=right[r].key):
                    final_output.append(left[l])
                    l+=1
                else:
                    final_output.append(right[r])
                    r+=1
            if(r<len(right)):
                final_output+=right[r:]
            if(l<len(left)):
                final_output+=left[l:]
            return final_output
        output=mergeSortHelper(pairs)
        return output

