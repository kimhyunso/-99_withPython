# 풀이 방법 1
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        # edges[0][0] == edges[1][0]
        # edges[0][0] == edges[1][1]
        # edges[0][0] == edges[2][0]
        # edges[0][0] == edges[2][1]
        
        # edges[0][1] == edges[1][0]
        # edges[0][1] == edges[1][1]
        # edges[0][1] == edges[2][0]
        # edges[0][1] == edges[2][1]
        
        for i in range(len(edges[0])):
            check_node = edges[0][i]
            for j in range(1, len(edges)):
                if check_node == edges[j][i]:
                    return check_node


# 풀이 방법 2
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()

