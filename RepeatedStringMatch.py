'''
686. Repeated String Match

Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
Example 2:

Input: a = "a", b = "aa"
Output: 2
Example 3:

Input: a = "a", b = "a"
Output: 1
Example 4:

Input: a = "abc", b = "wxyz"
Output: -1
 

Constraints:

1 <= a.length <= 104
1 <= b.length <= 104
a and b consist of lower-case English letters.

'''
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # code here
        if B in A:
            return 1
        if set(A)!=set(B):
            return -1
        c=1
        l1=len(A)
        l2=len(B)
        s=A
        loop=l2/l1
    
        while(c<=loop+2):
            s+=A
            c+=1
            if B in s:
                return c
                break
        return -1

        
