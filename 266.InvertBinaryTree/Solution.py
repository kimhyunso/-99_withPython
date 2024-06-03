from typing import Optional
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            temp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = temp

        return root


# 테스트 코드

left_node = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
right_node = TreeNode(7, TreeNode(6, None, None), TreeNode(9, None, None))
top_node = TreeNode(4, left_node, right_node)

# top_node = None

solution = Solution()
top_node = solution.invertTree(top_node)




