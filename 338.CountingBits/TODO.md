# 문제내용

매개변수로 넘겨준 숫자를 비트로 변환하고 변환된 비트를 더한 것을 배열에 담아 리턴한다.

![문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/791c07c2-931d-48d3-940c-72f76405d045)
{: .align-center}

# 풀이법
- `bin()` : 숫자를 비트로 변환시켜주는 함수
- `count(arg1)` : 해당 변수 안에서 arg1과 일치하는 문자의 갯수를 샌다.
- `replace(arg1, arg2)` : arg1을 arg2로 바꿔준다.
- 슬라이싱(slicing) : 인덱스를 통해 [~부터:~까지] 슬라이싱을 할 수 있다.

1. `bin()` 함수를 이용해서 bit로 변환시킨다. 
2. 변환된 숫자에서 `replace()` 함수또는 슬라이싱을 이용해서 0b 문자를 제거한다.
3. 해당 변수에서 1의 갯수를 샌다. 또는 해당 변수를 for문으로 돌려 전체의 합을 구한다.

```python
class Solution:
    # 첫번째 풀이법
    # def countBits(n: int) -> List[int]:
    #     result = []
    #     for num in range(n+1):
    #         bit_number = bin(num).replace('0b', '')
    #         count_sum = 0
    #         for i in range(len(bit_number)):
    #             count_sum += int(bit_number[i])
    #         result.append(count_sum)

    #     return result

    # 두번째 풀이법
    # def countBits(self, n: int) -> List[int]:
    #     result = []
    #     for num in range(n+1):
    #         result.append(bin(num).replace('0b', '').count('1'))

    #     return result

    # 세번째 풀이법
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            result.append(bin(num)[2:].count('1'))

        return result
```

