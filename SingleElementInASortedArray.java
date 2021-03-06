/*
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

*/

class Solution {
    public int singleNonDuplicate(int[] nums) {
        int low=0;
        int high=nums.length-1;
        if (high==low) return nums[0];
        if (nums[0]!=nums[1]) return nums[0];
        while(low<high)
        {
            int mid=low+(high-low)/2;
            if (nums[mid]!=nums[mid-1] && nums[mid]!=nums[mid+1]) 
                return nums[mid];  
            if (mid%2==1){
                if (nums[mid]==nums[mid-1]) low=mid+1;
                else high=mid-1;
            }
            else {
                if (nums[mid]==nums[mid+1]) low=mid+1;
                else high=mid-1;
            }
            
        }
        return nums[low];   
    }
}
