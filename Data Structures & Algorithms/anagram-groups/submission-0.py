class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets={}
        for x in strs:
            sorted_characters = sorted(x)
            sorted_text = "".join(sorted(sorted_characters))
            if sorted_text not in buckets:
                buckets[sorted_text]=[x]
            else:
                buckets[sorted_text].append(x)

        return list(buckets.values())
        
        