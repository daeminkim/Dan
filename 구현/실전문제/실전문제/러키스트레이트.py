n = input()
lenth =  len(n)

sum = 0

for i in range(lenth//2):  # 반으로 나누어서 앞쪽 숫자들의 합
    sum += int(n[i])
    
for i in range(lenth//2,lenth): # 앞쪽 숫자들에서 뒷쪽 숫자들을 순서대로 뺐음
    sum -= int(n[i])
# 0 이면은 앞쪽 숫자 뒤쪽 숫자의 합이 같아서 LUCKY, 아니면 READY
if sum == 0:  
    
    print('LUCKY')
else :
    print('READY')
