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