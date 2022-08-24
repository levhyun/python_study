# 비교연산자
# 1. ==
# 2. !=
# 3. <
# 4. <=
# 5. >
# 6. >=

print('1==1', 1==1)
print('1==2', 1==2)

print('1!=2', 1!=2)
print('1!=1', 1!=1)

print('1<2', 1<2)
print('2<1', 2<1)

print('1<=1', 1<=1)
print('1<=3', 1<=3)

print('2>1', 2>1)
print('1>2', 1>2)

print('1>=1', 1>=1)
print('3>=1', 3>=1)

# 변수 int 정수, float 실수, ord 문자

a = 1.1
b = ord('b')
print("\n\n정수형 변수 a값 =",int(a)) #1
print("\n실수형 변수 a값 =",float(a)) #1
print("\n문자형 변수 a값 =",chr(b),"\n") #1

# 입력 input

a=input("정수를 입력하세요>") # 변수 a에 값을 입력 받음
print(a)

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





