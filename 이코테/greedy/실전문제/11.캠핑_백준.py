l=5
p=8
v=17
# 간단한 수학문제 였고 규칙을 찾으면 금방 풀 수 있는 문제이다.
#  day = min(v%p,l) 연속할 수있는 날보다 나머지가 크게 나오면 연속할 수있는 날만큼만 머물 수 있다.
# https://www.acmicpc.net/problem/4796

i =1
while True:
    l,p,v = map(int,input().split())
    if l+p+v ==0:
        break
    day = min(v%p,l)            #이게 제일 포인트이다.
    day1 = v//p
    print(f'Case {i}:', (day1*l)+day)  
    i+=1