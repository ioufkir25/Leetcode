#Given the roots of two binary trees p and q, write a function to check if they are the same or not.

#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if  p is None and q is None:
            return True 
        if  p is None or q is None or p.val!=q.val :
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
           
