# 문제 설명
# 가끔 몇몇 작가들은 강조를 하기 위해서 과도하게 느낌표를 남발한다. 느낌표와 물음표를 섞어서 놀라움을 표시하는 경우도 있다. 예를 들자면 "정말 그렇게 생각해요??!!".
# 출판을 하려면 이런 식의 과도한 느낌표와 물음표의 남발을 고쳐야 된다. 만약 느낌표가 연속으로 여러 개가 사용 되었다면 한 개의 느낌표로 바꾸고, 느낌표와 물음표가 섞여있다면 하나의 물음표로 바꿔야 한다. 이렇게 고쳐진 문자열을 리턴하시오.

# 참고 / 제약 사항
# Document의 길이는 1이상 50이하다.
# Document는 알파벳, 공백, 물음표, 느낌표로만 이루어져있다.

# 테스트 케이스
document =   "a??a ?!a a!?b b!?!C C?!!D D?!?EE ??? FF!!! !???!"
#            a?a a? b?C ?!D ??EFF!!!
#리턴(정답): "a?a ?a a?b b?C C?D D?EE ? FF! ?"
#            
#document = " a b c A B ! !!C!!! ! ! !C ?!!? ?!? ??"
# 리턴(정답): " a b c A B ! !C! ! ! !C ? ? ?"            



# 못풀음 
# 앞 또는 뒤에 ? 있으면 느낌표 삭제 // 물음표 중복이면 1개로 압축 
# 느낌표 여러개 일때 1개로 압축
# 문자, 공백은 그대로 붙인다.

result = document[0]

for i in range(1,len(document)-1) :
    if document[i-1] == '?':
        if type(document[i]) == str or document[i] == " ":
                result = result + document[i]
        else:
            del document[i]
    # else:
    #     result = result + document[i]
print(result)

