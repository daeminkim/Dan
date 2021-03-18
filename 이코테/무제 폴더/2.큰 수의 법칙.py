# while 문을 쓰고 m 더하는 횟수를 감소시키면서  break 하면된다.
# n, m, k = map(int,input().split())
# num = list(map(int,input().split()))

n, m, k = 5, 8, 3
num = [2,4,5,4,6]

num.sort()
result = 0

while True:
    if m == 0:
        break
    for _ in range(k):
        if m == 0:
            break  # 더할때 마다 m-1을 해서 횟수를 줄인다.
        result += num[-1]
        m-=1
    if m==0:
        break
    result+=num[-2]
    m-=1
print(result)