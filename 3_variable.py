# 변수 int 정수, float 실수, ord 문자

a = 1.1
b = ord('b')
print("\n\n정수형 변수 a값 =",int(a)) #1
print("\n실수형 변수 a값 =",float(a)) #1
print("\n문자형 변수 a값 =",chr(b),"\n") #1

# 입력 input

a=input("정수를 입력하세요>") # 변수 a에 값을 입력 받음
print(a)

# 전역변수

gun = 10 # 전역변수 선언

def f():
    global gun # 전역 공간에 있는 gun변수를 사용한다는 선언
    print(gun)
    return 0