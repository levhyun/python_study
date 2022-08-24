# 문자열

s = '\n문자열'
print(s)
s2 = "작은따옴표든 큰따옴표든 상관없다."
print(s2)
s3 = """
큰 따옴표 세개를 적으면
여러줄을 쓸수있다."""
print(s3)
# 문자열 포맷

sp = "문자열 포맷"
sp2 = "문자열 포맷2"
print("문자열 %s" % "포맷")
print("문자열 포맷%d" % 20)
print("< %s >" % sp)
print("< %s > < %s >" % (sp,sp2))

print("format({})".format("포맷"))
print("format({}){}".format("포맷","입니다"))
print("format({text}){last}".format(text="포맷", last="입니다아아아"))

one = 1
two = 2
print(f"({one})one - ({two})two") # 참고:v3.6이상만 가능

# \r : 커서를 맨 앞으로 이동
# \b : 백스페이스 (한글자 삭제)
print("123\b45")
# \t : 탭
print("1\t2345")

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 변수명.lower() 는 변수명의 문자열 모두 소문자로 출력
print(python.upper()) # 변수명.upper() 는 변수명의 문자열 모두 대문자로 출력
print(python[0].isupper()) # 변수명[index번호].isupper() 는 변수명[index번호]에 해당하는 문자가 대문자이면 True 아니면 False 출력
print(len(python)) # 변수 안에 문자열길이 출력
print(python.replace("Python", "Mysql")) # 변수명.replace 는 함수괄호안에 첫번째 문자열이 변수안에 있다면 그문자열 자리에 두번째 문자열로 출력

index = python.index("n") # 변수 안에 문자열에서 인덱스 0번부터 n을 찾으면 출력하고 못 찾으면 오류남
print(index)
index = python.index("n", index + 1) # 변수 안에 문자열에서 인덱스 0번부터 n을 찾고 n이 있다면 그 자리에서 +1한 자리에서 다시 찾은후 출력하고 못 찾으면 오류남
print(index)

print(python.find("n")) # .index 함수와 동일하지만 find함수는 n을 못 찾았을탠 -1출력
print(python.find("Mysql")) # Mysql이란 단어가 python 변수안에 문자열에선 없어서 -1 출력

print(python.count("n")) # 변수안에 문자열중 n의 갯수 출력