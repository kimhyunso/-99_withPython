class Solution:
    def fib(self, n: int) -> int:
        memo = [1] * (n + 1)
        memo[0] = 0

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n] 
        


# 테스트 케이스
solution = Solution()

print(solution.fib(5))