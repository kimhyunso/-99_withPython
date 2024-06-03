from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 테스트 코드

left_node = TreeNode(9, None, None)
right_node = TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))
top_node = TreeNode(3, left_node, right_node)

# top_node = TreeNode(1, None, TreeNode(2, None, None))

solution = Solution()
result = solution.maxDepth(top_node)

print(result)










