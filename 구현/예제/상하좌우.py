n = 5
plans =['r','r','r','u','d','d']
move =['l','r','u','d']

x= 1
y=1
# 책 p.111 // 좌우로 움직일땐 y값만 , 위아래로 움직일땐 x값만 바뀐다.
dx = [0,0,-1,1]  
dy = [-1,1,0,0]
# 이동계획 하나씩 확인
for plan in plans:
    #이동후 좌표 구하기
    for i in range(len(move)):
        if plan == move[i]:
            nx = x+dx[i]
            ny = y+dy[i]

# 공간을 벗어나는 경우 무시 //  정사각형 사이즈 보고 정하면 될듯.. 이문제에선 1,1부터시작 n,n 가 마지막
    if nx <1 or ny <1 or ny>n or nx >n:
        continue  # 밑에 코드 실행안하고 건너뜀

# 이동 수행
    x,y = nx, ny
print(x,y)    
