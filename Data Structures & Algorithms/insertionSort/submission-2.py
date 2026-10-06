# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        visited=[]
        index=0
        for i in range(len(pairs)):
            j=i-1
            while i>0 and pairs[i].key<pairs[j].key:
                pairs[i],pairs[j]=pairs[j],pairs[i]
                i-=1
                j=i-1
            visited.append(pairs[:])
        return visited



