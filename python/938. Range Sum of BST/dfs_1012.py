# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#ans = 0

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    #      10
    #    /    \
    #   5     15
    #  / \    / \
    # 3   7  n   18
    
    
        def dfs(root: TreeNode) -> None:
            if root:
                if L <= root.val and root.val <= R:
                    self.ans += root.val
                if L < root.val:
                    dfs(root.left)
                if root.val < R:
                    dfs(root.right)
        
        self.ans = 0
        dfs(root)
        return self.ans
            
            
