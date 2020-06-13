'''
Given an integer array nums, find the contiguous subarray (containing at least
 one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using 
the divide and conquer approach, which is more subtle.'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum_till_now,max_sum=0,0
        for i in range(len(nums)):
            sum_till_now=sum_till_now+nums[i]
            if sum_till_now<0:
                sum_till_now=0
            if sum_till_now>max_sum:
                max_sum=sum_till_now
        if max_sum<=0:
            return max(nums)
        return max_sum
                
        