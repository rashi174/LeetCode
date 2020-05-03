"""
318. Maximum Product of Word Lengths
Add to List

Share
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(reverse=True)
        ans = 0
        for i in range(0,len(words)-1):
            for j in range(i+1,len(words)):
                d = set(words[i]) & set(words[j])
                if len(d) == 0:
                    ans = max(ans,len(words[i])*len(words[j]))
                    
        return ans