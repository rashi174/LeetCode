#https://leetcode.com/problems/even-odd-tree/   (Medium Level)

'''

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
>>For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
>>For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue=[root]
        level=[]
        while (len(queue)>0):
            templ=[]
            for i in range(0,len(queue)):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                templ.append(queue.pop(0).val)
            level.append(templ)
        if level[0][0]%2!=1:
            return False
        def oddlevels(list1):
            for i in list1:
                if i%2==1:
                    return False
            return list1==sorted(set(list1))[::-1]  
        def evenlevels(list1):
            for i in list1:
                if i%2==0:
                    return False
            return list1==sorted(set(list1))  
        ans=[]
        for i in range(len(level)):
            if i%2==0:
                ans.append(evenlevels(level[i]))
            else:
                ans.append(oddlevels(level[i]))
        return all(ans)
        
