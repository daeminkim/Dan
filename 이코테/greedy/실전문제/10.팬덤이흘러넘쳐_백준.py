#https://www.acmicpc.net/problem/17262
# n=3
# go=[2,1,2]
# back=[5,4,4]
n=2
go=[1,5]
back=[4,6]
# for _ in range(3):
#     A=list(map(int,input().split(" ")))
#     go.append(A[0])
#     back.append(A[1])
go1=sorted(go)[-1]
back1=sorted(back)[0]
if go1- back1 <= 0:
    print(0)
else :
    print(go1-back1)
