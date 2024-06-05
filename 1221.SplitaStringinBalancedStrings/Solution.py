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