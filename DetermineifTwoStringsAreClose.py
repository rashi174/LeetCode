class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        hashmap1={}
        for i in word1:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
                
        hashmap2={}
        for i in word2:
            if i in hashmap2:
                hashmap2[i]+=1
            else:
                hashmap2[i]=1
        if hashmap1.keys()==hashmap2.keys():
            l=list(hashmap1.values())
            l2=list(hashmap2.values())
            return sorted(l)==sorted(l2)
