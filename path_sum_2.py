class Solution(object):
    def pathSumUtil(self, root, currentSum, total, 
                    path, result):
        
        if not root:
            return
        
        currentSum += root.val
        path.append(root.val)
        
        if not root.left and \
        not root.right and \
        currentSum == total:
            result.append(path[:])
            path.pop()
            return
        
        self.pathSumUtil(root.left, currentSum, total, path, result)
        self.pathSumUtil(root.right, currentSum, total, path, result)
        path.pop()
        currentSum -= root.val
        
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type total: int
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        result = []
        path = []
        
        self.pathSumUtil(root, 0, total, path, result)
        
        return result