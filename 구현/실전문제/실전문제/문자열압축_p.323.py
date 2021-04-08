s = 'abcabcdede'  #10개
def solution(s):
    answer = len(s) # 압축후 문자열중 가장짧은 문자열의 개수
    unit = 1
    while unit <= len(s)//2:
        word = ''  # 압축 후 문자열
        count = 1  # 문자열 반복되는 값
        comp = s[:unit] # 잘린 문자열
        for i in range(unit, len(s), unit):
            if comp == s[i: i+unit]:
                count += 1
            else:
                if count == 1:
                    word += comp
                else:
                    word += (str(count) + comp)
                comp = s[i: i+unit]
                count = 1

        if count == 1:
            word += comp
        else:
            word += str(count) + comp

        unit += 1
        answer = min(len(word), answer)

    return answer

print(solution(s))