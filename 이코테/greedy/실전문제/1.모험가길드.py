# n = int(input())
# k = list(map(int,input().split(" ")))

n= 5
data = [2,3,1,2,2]

data.sort() # 원본 변경 / True 가 내림차순이다.
result = 0  # 그룹 갯수 
count = 0 # 모험가의 수 
"""
1. 기본 로직은 공포도가 작은 탐험가 부터 (숫자가 작은) 그룹을 이뤄 나가는것이다.
2. count 에 일단 모험가를 1개 넣어주고 다음 모험가(i)가 1보다 작거나 같으면 그룹이 되어나간다.
3. 1보다 크다면 count가 초과 되지 않고 다시 반복문으로 올라가서 다음 모험가를 데리고 count 에 1을 더해준다.
4 . 그러면서 조건에 만족할때 그룹개수를 증가시킨다.
"""
for i in data:
    count +=1
    if count >= i:
        result +=1
        count=0
print(result)








# 첫번째 코드 실패 // 
# (4,3,2,2,2,1,1,1,1,1) 이 케이스를 입력했을때 4,3,2가 남으면 더이상 그룹이 될 수없는데 그냥 실행이된다. 
# 
#  
# while True:
#     m = min(k)
#     for _ in range(m):
#         k.pop()
#     count += 1
#     if len(k)==0:
#         break
# print(count)
