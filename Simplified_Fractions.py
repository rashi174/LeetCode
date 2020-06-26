#https://leetcode.com/contest/biweekly-contest-26/problems/simplified-fractions/
'''
 Simplified Fractions

Difficulty:Medium
Given an integer n, return a list of all simplified fractions between 0 and 1
 (exclusive) such that the denominator is less-than-or-equal-to n.
 The fractions can be in any order.

 

Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]
Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
Example 4:

Input: n = 1
Output: []

'''

from fractions import Fraction 

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n==1:
            return []
        li=[]
        for i in range(1,n):
            for j in range(i,n+1):
                if i/j<=1:
                    li.append(str(Fraction(i,j)))
        li=list(set(li))            
        if '1' in li:
            li.pop(li.index('1'))
        return sorted(li)
                
            
        