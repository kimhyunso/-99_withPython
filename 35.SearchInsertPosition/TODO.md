# 문제 내용

nums 리스트 안에 target이 있다면 target의 인덱스 번호를 리턴


target이 nums 리스트 안에 없다면 

1. 왼쪽 : 1을 리턴
2. 오른쪽 : 배열의 길이를 리턴

![문제내용](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/25d1004f-cbe5-4467-a1ae-a5fad2a87f2c)
{: .align-center}

# 문제 풀이
이진 탐색을 통해 풀이함

1. left : 배열의 0번째 인덱스 / right : 배열의 길이 - 1 선언 
2. left가 right 이하일때만 반복
3. mid = (left + right) // 2로 초기화
4. 1.1. nums[mid]에 있는 값이 target과 같다면 mid(=index) 리턴
5. 1.2. nums[mid]에 있는 값이 target보다 크다면 right = mid - 1 연산
6. 1.3. nums[mid]에 있는 값이 target보다 작다면 left = mid + 1 연산
7. 2번 반복
8. left 리턴 (left값은 항상 배열의 맨마지막 + 1이거나 1이 된다.)

## left 일때 예시
![left](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/e5241964-08fc-445b-b960-2b4e62a6a458)
{: .align-center}


## right 일때 예시
![right](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/af96cd72-b94d-4eb6-8f13-f40c4a76f7bc)
{: .align-center}


```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return left
```










