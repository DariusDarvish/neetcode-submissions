class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        def isPrefixAndSuffix(s1,s2):
            print('s1',s1)
            print('s2',s2)
            print("prefix",s1[:len(s2)]==s2)
            print("suffix",s1[-len(s2):]==s2)
            if s1[:len(s2)]==s2 and s1[-len(s2):]==s2:
                print('match {} {}'.format(s1,s2))
                return True
            else:
                return False
        for i in range(len(words)):
            for j in range(len(words)):
                print("i={} j={}".format(i,j))
                if i<j and isPrefixAndSuffix(words[j],words[i]):
                    count+=1
            
        
        return count

            