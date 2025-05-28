# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        def reverse(root1, root2, level):
            if root1 is None and root2 is None:
                return None

            if level %2 != 0:
                root1.val, root2.val = root2.val, root1.val
            #moving towards the outer nodes of the next level
            reverse(root1.left, root2.right, level+1)
            #moving towards the inner nodes of the next level.
            reverse(root1.right, root2.left, level+1)

        reverse(root.left, root.right, 1)
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        v=[root]
        l=0
        while v:
            l+=1
            vc=[]
            for i in v:
                if(i.left):
                    vc+=[i.left]
                if(i.right):
                    vc+=[i.right]
            if(l%2==1):
                for i in range((len(vc)+1)//2):
                    vc[i].val,vc[len(vc)-i-1].val=vc[len(vc)-i-1].val,vc[i].val
            v=vc
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        def reverse(a, b, is_odd=False):
            if a is None or b is None:
                return
            if is_odd:
                a.val, b.val = b.val, a.val
            reverse(a.left, b.right, not is_odd)
            reverse(a.right, b.left, not is_odd)

        reverse(root.left, root.right, is_odd=True)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        ans = []
        q = [root]
        k = 0
        while q:
            l = []
            for i in range(len(q)):
                d = q.pop(0)
                if d.left:
                    q.append(d.left)
                if d.right:
                    q.append(d.right)
                l.append(d.val)
            if k%2 == 0:
                ans.extend(l)
            else:
                ans.extend(l[::-1])
            k+=1
        def insertLevelOrder(arr, i, n):
            root = None
            if i < n:
                root = TreeNode(arr[i]) # type: ignore
                root.left = insertLevelOrder(arr, 2 * i + 1, n)
                root.right = insertLevelOrder(arr, 2 * i + 2, n)

            return root
        root = None
        n = len(ans)
        root = insertLevelOrder(ans,0,n)
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        l=1
        q=[root]

        while q:
            node=q.pop(0)
            l+=1
            if node.left:
                q.append(node.left)
                q.append(node.right)
            if (l&(l-1))==0 and l%3==2:
                for i in range(len(q)//2):
                    q[i].val,q[-1-i].val=q[-1-i].val,q[i].val

        return root