class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        def isPrefixAndSuffix(s1,s2):
            if s1[:len(s2)]==s2 and s1[-len(s2):]==s2:
                return True
            else:
                return False
        for i in range(len(words)):
            for j in range(len(words)):
                if i<j and isPrefixAndSuffix(words[j],words[i]):
                    count+=1
            
        
        return count

            