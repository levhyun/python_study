# 조건문
# if - 조건이 일치한다면 실행
# else - 조건이 불일치하다면 실행
# if ~ else ~ 기본 조건문 완전체
# if ~ if ~ ..... else ~ 중첩 조건문

a=1
b=2
c=2

# 완전체 조건문
if a!=b:
    print("a!=b")
else:
    print("a==b")

# 중첨조건문
if a!=b:
    if b==c:
        print("a!=b==c")
    else:
        pass
else:
    pass
