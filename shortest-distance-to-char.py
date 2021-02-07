'''
821. Shortest Distance to a Character

Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

 

Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]
 

Constraints:

1 <= s.length <= 104
s[i] and c are lowercase English letters.
c occurs at least once in s.

'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indx=[i for i in range(len(s)) if s[i] == c]
        list1=[i for i in range(len(s))]
        l=[]
        for i in range(len(list1)):
            l.append(min([abs(x-i) for x in indx]))
        return l
