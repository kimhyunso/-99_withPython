# 문제내용
숫자만큼 파스칼 삼각형을 만들어 리턴해야한다.

파스칼 삼각형은 아래와 같다.

![PascalTriangleAnimated2](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/a020a4a1-546f-4380-8a08-7aa5b1668358)
{: .align-center}

# 풀이법

n = 5일때, 아래와 같은 패턴을 띈다.

1. 리스트를 [1]*n 만큼 초기화 해놓는다. (=리스트 컴프리헨션)

```python
lists = [
    [1],                # index = 0
    [1, 1],             # index = 1
    [1, 1, 1],          # index = 2 
    [1, 1, 1, 1]        # index = 3
    [1, 1, 1, 1, 1]     # index = 4
]
```
2. 2번째 이전은 더하는 과정이 없으므로 생략한다. 이미 1번에서 만들어졌음
3. 리스트는 전부 1로 초기화 되어있기 때문에 아래와 같은 패턴이 나타난다.

```python
lists[2][1] = lists[1][0] + lists[1][1]
# ---------------------------------------
lists[3][1] = lists[2][0] + lists[2][1]
lists[3][2] = lists[2][1] + lists[2][2]
# ---------------------------------------
lists[4][1] = lists[3][0] + lists[3][1]
lists[4][2] = lists[3][1] + lists[3][2]
lists[4][3] = lists[3][2] + lists[3][3]
```
즉, 첫번째 인덱스는 2부터 시작하여 4가 마지막이 되고 두번째 인덱스는 1부터 점차증가한다.

### **`range()`는 0부터 n-1까지 돈다.**

```python
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * i for i in range(1, numRows+1)]
		
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp

s = Solution()
print(s.generate(5))
```






