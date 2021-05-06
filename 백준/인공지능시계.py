h, m, s = map(int,input().split())
S = int(input())

s1 = (S+s)%60   # 최종 초
m1 = (S+s)//60  # 몫을 다 분에 더하고 그걸 또 60 으로 나누고 반복해서 최종 분, 시를 만든다.

m2 = (m+m1)% 60 # 최종 분
h1 = (m+m1)//60

h2 = (h1+h)%24 # 최종 시간

print(h2,m2,s1)