# 문제내용

체육복을 갖고온 사람 중 몇 명이 체육복을 도둑맞았다. => lost리스트

여벌의 체육복을 갖고온 사람이 있다. => reverse리스트

여벌의 체육복을 가져온 사람은 체육복을 도둑맞은 사람에게 빌려줄 수 있다.

단, 만약 5명 중 3번째 사람이 도둑 맞았다면 2번째 사람과 4번째 사람 즉, 양옆에 있는 사람들에게만 빌릴 수 있다.

전체 학생의 수 2 <= x >= 30 : 2명 이상 30명 이하 :: n^2의 스케일도 풀 수 있는 문제 30^2 = 900

![체육복 문제](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/439e8dce-1ccb-4602-acb1-57ccc7e6a56e)
{: .align-center}

# 풀이법
1. 체육복을 명 수 만큼 초기화한다. (일단, 전부 체육복을 가지고 왔기 때문에 예시)[1 1 1 1 1]로 초기화)
2. 체육복을 잃어버린 사람, 체육복 여벌을 갖고 온 사람들을 정렬한다.
3. 체육복을 잃어버린 사람과 체육복의 여벌을 갖고 온 사람 중 같은 사람이 있다면 제거한다 (중복제거).
4. 체육복을 잃어버린 사람 중 왼쪽과 오른쪽에 체육복의 여벌을 갖고온 사람이 있는지 체크한다. (예시 : [1 2 0 2 1] : 3번의 입장에서는 2,4번이 체육복을 갖고옴)
    - 있다면 : 체육복의 여벌을 갖고온 사람에게 빌린다. -1 / 체육복을 잃어버린 사람이 체육복을 얻는다. +1 => [1 1 1 2 1] 
    - 없다면 : 아무것도 하지 않는다.
5. 체육복을 갖고 있는 리스트에서 1이상인 데이터의 갯수를 샌다.

```python
def solution(n, lost, reserve):

    uniform = [1] * n
    lost.sort()
    reserve.sort()

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
```






