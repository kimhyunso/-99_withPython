# 문제내용
FALSE = 0
TRUE = 1
OR = 2
AND = 3

![2331번문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/6f6b3c30-d571-419f-a68f-cccb73bd2433)
{: .align-center}

위와 같이 작동한다.

**리프 노드 : 맨마지막에 있는 자식이 없는 노드**

리프 노드 왼쪽과 오른쪽에 `False` 혹은 `True`가 있다면 부모 노드의 값을 보고 연산하여 진행한다.


# 풀이법
재귀함수를 사용하여 문제를 해결했다.

TreeNode를 아래 테스트 케이스와 같이 초기화하여 진행하였다.

> 현재 노드의 왼쪽과 오른쪽이 있는지 판단한다.
>
> 왼쪽과 오른쪽 노드가 있다면 현재 노드의 값을 체크하여 값이 2 또는 3이라면 다시 1번으로 돌아가 진행한다.
> 
> 왼쪽 또는 오른쪽이 없다면 (=리프노드) 현재 노드의 값을 `boolean`형태로 변환하여 반환한다. (무조건 `True` 혹은 `False`가 나옴)
>
> 모든 재귀를 마치면 1-1 부분의 값체크하는 부분을 실행하여 `or` 또는 `and` 연산을 진행한다.

```python
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
```






