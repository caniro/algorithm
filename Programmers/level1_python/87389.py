# 나머지가 1이 되는 수 찾기 : https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 0
    if n % 2:
        answer = 2
    else:
        for i in range(3, n):
            if n % i == 1:
                answer = i
                break
    return answer
