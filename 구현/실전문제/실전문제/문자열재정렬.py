#P.322
n = input()
result = []
value = 0

for i in range(len(n)):
    if n[i].isalpha():  # isalpha  - 알파벳이면 리스트에 추가
        result.append(n[i])
    else:               # 알파벳이아니면 더함
        value += int(n[i])

result.sort()            

result.append(str(value))

print(''.join(result))
