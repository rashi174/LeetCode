#Leaf-Similar Trees


'''

Consider all the leaves of a binary tree.  From left to right order, the values 
of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200

'''

class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
    
'''
#872. Leaf-Similar Trees


def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    ls1 = []
    ls2 = []
    self.leaves(root1, ls1)
    self.leaves(root2, ls2)
    
    return ls1 == ls2


def leaves(self, root, ls):
    if root:
        if not root.left and not root.right:
            ls.append(root.val)
        else:
            self.leaves(root.left, ls)
            self.leaves(root.right, ls)
'''