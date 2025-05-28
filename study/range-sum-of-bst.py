# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0

        if root.val > high:
            return self.rangeSumBST(root.left,low,high)
        if root.val < low:
            return self.rangeSumBST(root.right,low,high)

        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)


class Solution:
    def rangeSumBST(self, n: Optional[TreeNode], l: int, h: int) -> int:
        return self.rangeSumBST(n.left,l,h)+n.val*(l<=n.val<=h)+self.rangeSumBST(n.right,l,h) if n else 0