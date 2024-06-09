# 문제내용
엘리스와 밥은 게임을 한다.

게임은 엘리스가 먼저 시작하며, 엘리스와 밥은 자신이 선택한 x만큼 움직일 수 있다. 단, 아래와 같은 조건이 있다.

- $0 < x < n$ and $x$ % 2 == 0

x만큼 움직이면 $n - x$ 만큼 n의 숫자가 줄어든다.

단, 엘리스와 밥은 최선의 선택만을 한다.

### 예시

n = 3

엘리스먼저 1칸을 움직이고, 밥이 1칸을 움직여서 엘리스는 다음칸을 움직일 수 없게됨 따라서, 엘리스의 패배


![문제예시](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/6cf3bcb4-5baa-46ea-a7da-e0b924901ddf)
{: .align-center}

엘리스가 패배하면 `False`를 이긴다면 `True`를 리턴하라

# 풀이법
아래 이미지와 같이 n의 경우를 트리구조로 만들어보았다.

### n = 4일때
엘리스가 이김
![트리4](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/12de76aa-4d08-45ba-94c7-f29f3bb59bdf)
{: .align-center}
### n = 5일때
밥이 이김
![트리5](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/a0b20fcd-62df-40fa-8c7a-eea710e29c37)
{: .align-center}
### n = 6일때
엘리스가 이김
![트리6](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/833b0fd4-242b-4f81-90e5-9a1d3534ec9b)
{: .align-center}
### n = 7일때
밥이 이김
![트리7](https://github.com/kimhyunso/sail-99_withPython/assets/87798982/eabdfc0b-f69c-4ba0-b0f5-cd4b0eb1da58)
{: .align-center}

이런 패턴을 생각할 때 n이 1부터 7까지 엘리스와 밥이 돌아가며 이긴다는 패턴이 보였다.

따라서 짝수일 때에는 엘리스가 이기고, 홀수 일때는 밥이 이긴다.

```python
# 첫번째 풀이
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        else:
            return False

# 두번째 풀이
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
```






