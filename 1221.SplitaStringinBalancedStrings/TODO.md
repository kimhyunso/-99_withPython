# 문제내용
문자열이 밸런스가 있다.

L의 갯수와 R의 갯수가 같은지 판단한다.

## 예시
![예시내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/172b2e6d-9c58-4936-b2e3-c7c364920afb)
{: .align-center}

만약 RLRRLLRLRL이라면 RL -> 1, RRLL -> 2, RL -> 3, RL -> 4 로서 4가된다.

# 풀이법
스택을 사용하여 풀었다.

전의 문자 : prev_word / 현재 문자 : word

1. 문자를 스택에 push를 한다.
2. 전에 문자가 있는지 판단 후 전의 문자와 현재 문자가 같은지 판단한다.
3. 같다면 스택에 있는 데이터를 pop한다.
4. 다르면서 전의 문자가 비어있다면(= '') 스택에 push를 한 후 전의 문자를 비어준다.
5. 만약 스택이 비어있다면 갯수를 새고 전의 문자를 비어준다.
6. 다르다면 스택에 있는 데이터를 pop한다.

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        stack = []

        prev_word = ''

        for word in s:
            stack.append(word)
            if prev_word and prev_word != word:
                stack.pop()
         
            elif prev_word:
                stack.append(prev_word)
                prev_word = ''
                
            if not stack:
                answer += 1
                prev_word = ''
            else:
                prev_word = stack.pop()
                
        return answer

# 테스트 코드
solution = Solution()
solution.balancedStringSplit('RLRRLLRLRL')
```






