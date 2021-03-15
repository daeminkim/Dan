#data =list(input())

#data = [0,2,9,8,4]
#data = [5,6,7]
data = [0,2,4,0,3,4,5,0]

"""
1. 0은 더하기를 해도 아무 변화없다. 하지만 곱하기를 하면 0 이되서 최고 큰 수가 될 수 없다.
2. 곱하기는 순서를 어떻게 해도 상관없다.
3. 0을 아예 없앤다. //그리고 나머지 다 곱한다.
"""

data.sort()
result =1
for i in data:
    if 0 in data:
        data.remove(0) # remove는 중간에 껴있는 0을 지우지 못 한다. 그래서 정렬을 해서 0을 앞으로 다빼냈다.
        data = data
for i in data:
    result*=i
print(result)

