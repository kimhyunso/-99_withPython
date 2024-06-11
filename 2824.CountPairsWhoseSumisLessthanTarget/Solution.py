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
    



solution = Solution()
print(solution.countPairs([-6,2,5,-2,-7,-1,3], -2))
