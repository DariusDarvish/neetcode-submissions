class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count={}
        final_output=[]
        count=0
        for num in nums:
            if num not in frequency_count:
                frequency_count[num]=0
            frequency_count[num]+=1
   
        sorted_dict = {k: v for k, v in sorted(frequency_count.items(), key=lambda item: item[1],reverse=True)}
        for key in sorted_dict.keys():
            if count<k:
                final_output.append(key)
                count+=1
        return final_output

            
