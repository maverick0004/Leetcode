class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def f(root):
            
            if not root:
                return
            
            
            if root.left and not root.left.left and not root.left.right:
                f.total += root.left.val
            
            f(root.left)
            f(root.right)
        
        f.total = 0
        f(root)
        return f.total