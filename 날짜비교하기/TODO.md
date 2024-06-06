# 문제내용 

date1의 날짜가 date2의 날짜보다 작다면 1을 아니라면 0을 리턴하는 문제이다.

단, date1과 date2는 리스트 형태로 매개변수를 받는다.

date1 : [year, month, day] / date2 : [year, month, day]

![문제내용](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/746f7d6b-b42d-4221-8e39-a00b9f110b1f)
{: .align-center}

# 풀이법
1. date1과 date2의 년도를 판단하여 date1이 작다면 1을 크다면 0을 리턴한다.
2. 다음 판별식에 도착했다는 것은 date1의 년도와 date2의 년도가 같다는 의미이다
3. date1와 date2의 월을 비교한다. date1이 작다면 1을 크다면 0을 리턴한다.
4. 다음 판별식에 도착했다는 것은 date1의 월과 date2의 월이 같다는 의미이다.
5. date1과 date2의 일을 비교한다. date1이 작다면 1을 크다면 0을 리턴한다.

```python
# 첫번째 방법
def solution(date1, date2):
    if date1[0] < date2[0]:
        return 1
    elif date1[0] > date2[0]:
        return 0
    
    if date1[1] < date2[1]:
        return 1
    elif date1[1] > date2[1]:
        return 0
# 두번째 방법
def solution(date1, date2):
    for i in range(len(date1)):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0
    return 0
```