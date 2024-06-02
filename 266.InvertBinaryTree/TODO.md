# 문제내용
밑의 왼쪽 그림과 같이 트리가 있을 때, 오른쪽 그림 처럼 바꾸어라

![266번문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/bc94a1ea-8784-454e-8f11-f49404898ab9)
{: .align-center}


# 풀이법
재귀함수를 사용하여 문제를 해결했다.

> 테스트 케이스에 아무것도 없는 빈 배열 `[]`이 포함되어 있었기 때문에 root가 있어야만 했다.
>
> 


```python
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
```






