# 문제내용
밑의 왼쪽 그림과 같이 트리가 있을 때 깊이를 구하여라

![104번문제](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/a4e39275-7a59-4e56-a94b-ad02d63dc802)
{: .align-center}

# 풀이법
재귀함수를 사용하여 문제를 해결했다.

> 첫번째. 왼쪽 노드의 갯수를 샌다
>
> 두번째. 오른쪽 노드의 갯수를 샌다.
>
> 세번째. 왼쪽 노드와 오른쪽 노드 둘 중 큰 값을 고른다. + 1 (루트 노드를 새지 않았기 때문에 **중요**)

```python
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
```






