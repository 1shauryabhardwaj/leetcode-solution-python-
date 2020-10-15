#link : https://leetcode.com/problems/validate-binary-search-tree/submissions/

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def traverse(root, low, high):
            if not root:
                return True
            elif not low < root.val < high:
                return False
            return traverse(root.left,low, root.val) and traverse(root.right,root.val, high)
        return traverse(root,low=float('-inf'), high=float('inf'))