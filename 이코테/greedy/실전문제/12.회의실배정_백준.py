n = int(input())
st = []
for i in range(n):
    s,e= map(int,input().split())
    st.append([s,e])

st.sort(key = lambda x: (x[0],x[1]))

last =0
count = 0
for i,j in st:
    if i >=last:
        count+=1
        last = j
print(count)

# 백준 정답

# n = int(input())
# s = []
# for i in range(n):
#     first, second = map(int, input().split())
#     s.append([first, second])
# s = sorted(s, key=lambda a: a[0])
# s = sorted(s, key=lambda a: a[1])
# last = 0
# cnt = 0
# for i, j in s:
#     if i >= last:
#         cnt += 1
#         last = j
# print(cnt)