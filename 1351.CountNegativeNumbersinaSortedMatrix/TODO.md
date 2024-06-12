# 문제내용

해당 2차원 배열 요소 중 음수인 데이터의 갯수를 카운팅하여 리턴하라


![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/7bb9759a-5cd9-42f3-951c-181c995d33df)
{: .align-center}

# 풀이방법

해당 요소들을 하나 하나씩 확인하면서 0보다 작을 경우 카운팅을 한다.

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for nums in grid:
            nums.sort()
            for num in nums:
                if num < 0:
                    count += 1
                else:
                    break
        return count
```

### 이분 탐색법을 활용한 풀이

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        for row in grid:
            left, right = 0, n - 1
            while left <= right:
                mid = (right + left) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += (n - left)
        return count
```