def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    uniform = [1] * n

    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    for index in reserve:
        uniform[index - 1] += 1

    for index in lost:
        uniform[index - 1] -= 1
    
    for index in lost:
        if index - 2 >= 0 and uniform[index - 2] == 2:
            uniform[index - 2] -= 1
            uniform[index - 1] += 1
        elif index <= len(uniform) - 1 and uniform[index] == 2:
            uniform[index] -= 1
            uniform[index - 1] += 1
       
    
    answer = 0
    for i in uniform:
        if i >= 1:
            answer += 1
    
    return answer

result = solution(5, [4, 5], [3, 4])
print(result)