knight = 'a1'

k_list=[(2,-1),(2,1),(-2,1),(-2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]

# y = int(ord(knight[0]))
y = int(ord(knight[0]))-int(ord('a'))+1 # ord : 문자를 아스키 코드를 이용해서 숫자로 바꾼다.
x = int(knight[1])

cnt =0 

for k in k_list:
    y_n = y+k[1]
    x_n = x+k[0]

    if  (1<=y_n<=8) and (1<=x_n<=8):
        cnt +=1
print(cnt)
    
    