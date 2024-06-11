# 첫번째 풀이
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
# 두번째 풀이
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
        