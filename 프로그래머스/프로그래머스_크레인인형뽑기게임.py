board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	

# https://programmers.co.kr/learn/courses/30/lessons/64061
# 핵준특 1번 스택 리스트

# 문제 이해하기 ..
"""
board 는 2차원 배열
moves 1차원 배열 / 1번 위치 index =0 
숫자가 있는데 까지 반복해서 뽑고 그자리 숫자는 0으로 바뀜. 
bucket 에 연속으로 같은 값이 쌓이면 없어지면서 count +=2

# 문제 조각내기 
1) moves 앞에서 부터 순서대로 위치 이동.(Queue)사용
2) 해당위치에서 0이 아닌 숫자가 나올 때까지 아래 방향으로 탐색
3) 바닥에 도착하기 전 0이 아닌 숫자 발견시, 1.해당위치를 0으로 바꿈 2.해당숫자 바구니(bucket)에 담음
4) 바구니 가장위에 있는 숫자와 비교해서 서로다른숫자면 쌓고 같은 숫자이면 사라지게 함..그리고 사라진인형숫자 증가~!

pop():마지막원소 제거, popleft():첫번째 원소 제거 -->list는 pop은 사용가능하지만 popleft는 없다. 
"""
from collections import deque
moves = deque(moves)
bucket = []
cnt = 0
while moves:
    move = moves.popleft()
    for i in range(len(board)):
        doll = board[i][move-1]
        if doll != 0:
            board[i][move-1] = 0
            if bucket and bucket[-1] == doll :
                bucket.pop()  # 쌓기전이기때문에 pop
                cnt +=2

            else:
                bucket.append(doll)

            break # 0이아닌 인형을 만났을때 더이상 아래방향으로 탐색 필요없으니까 for문 탈출 
print(cnt)

# 프로그래머스 답
# from collections import deque
# def solution(board, moves):
#     moves = deque(moves)
#     bucket = []
#     cnt = 0
#     while moves:
#         move = moves.popleft()
#         for i in range(len(board)):
#             doll = board[i][move-1]
            
#             if doll != 0:
#                 board[i][move-1] = 0
                
#                 if bucket and bucket[-1] == doll :
#                     bucket.pop()  # 쌓기전이기때문에 pop
#                     cnt +=2

#                 else:
#                     bucket.append(doll)

#                 break # 0이아닌 인형을 만났을때 더이상 아래방향으로 탐색 필요없으니까 for문 탈출 
#     return cnt