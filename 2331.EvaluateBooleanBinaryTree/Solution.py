from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        value = root.val

        if left and right:
            if value == 2:
                return bool(self.evaluateTree(left) or  self.evaluateTree(right))
            elif value == 3:
                return bool(self.evaluateTree(left) and self.evaluateTree(right))

        return bool(value)

        
# 테스트 케이스
solution = Solution()

left_node = TreeNode(1, None, None)
right_node = TreeNode(3, TreeNode(0, None, None), TreeNode(1, None, None))
top_node = TreeNode(2, left_node, right_node)

# top_node = TreeNode(0, None, None)
result = solution.evaluateTree(top_node)

print(result)
