# 문제 내용
숫자 리스트 nums가 주어진다.

숫자 리스트 안에서 두 숫자를 더해 target보다 작다면 카운팅을 한다.

**nums의 길이는 1이상 50이하**

### 예시
![문제예시](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/6fbfd72d-5e95-4a96-a9aa-df2ba7656545)
{: .align-center}

# 문제 풀이
완전 탐색을 이용해 풀이함

nums의 길이가 50을 초과할 수 없다는 조건을 보고 n^2의 시간이 걸려도 풀 수 있다는 판단

1. nums의 길이만큼 반복
2. 1번의 반복 + 1 부터 nums의 길이 부터 반복
3. 만약 두 합계가 target보다 작을 시 카운팅

```python
from typing import List

# 완전 탐색 풀이
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
                    break

        return count
```








