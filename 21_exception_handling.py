# 예외처리

try:
    num = []
    num.append(int(input()))
    num.append(int(input()))
    # num.append(int(num[0]*num[1]))
    print("{}".format(num[2]))

except ValueError as arr: # arr = 에러명 (ValueError = 에러명령어)
    print(arr) # 에러명 출력

    # 일반 명령어 실행 가능 공간

except ZeroDivisionError as arr:
    print(arr)

except Exception as arr: # 실행 하면 list index out of range 발생
    print(arr)           # 왜냐하면 try함수안에 num[2]값이 없기 때문