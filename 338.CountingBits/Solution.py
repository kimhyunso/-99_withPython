from typing import List
# 1
class Solution:
    # 1
    # def countBits(n: int) -> List[int]:
    #     result = []
    #     for num in range(n+1):
    #         bit_number = bin(num).replace('0b', '')
    #         count_sum = 0
    #         for i in range(len(bit_number)):
    #             count_sum += int(bit_number[i])
    #         result.append(count_sum)

    #     return result

    # 2
    # def countBits(self, n: int) -> List[int]:
    #     result = []
    #     for num in range(n+1):
    #         result.append(bin(num).replace('0b', '').count('1'))

    #     return result

    # 3
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            result.append(bin(num)[2:].count('1'))

        return result


result = countBits(5)
print(result)