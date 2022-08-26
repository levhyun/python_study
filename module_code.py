# 모듈코드

def select(num): # 23_module 파일에서 호출되어 매개변수를 받고 코드 실행
    if num == 1:
        adult()
    elif num == 2:
        student()
    elif num == 3:
        baby()
    else:
        exit(0)


def adult():
    print("내실 금액 : 13500원")


def student():
    print("내실 금액 : 10000원")


def baby():
    print("내실 금액 : 5000원")
