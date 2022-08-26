# 에러발생시키기

try:
    a = int(input("1~10 : "))
    if a > 10:
        raise ValueError

except ValueError:
    print("10초과!")

# 사용자 정의 에러

class BigNumberError(Exception):
    pass

try:
    a = int(input("1~10 : "))
    if a > 10:
        raise BigNumberError

except BigNumberError:
    print("big_number_error")

# finally 무조건 실행됨

try:
    a = int(input("1~10 : "))
    if a > 10:
        raise ValueError

except ValueError:
    print("10초과!")

finally:
    print("무조건 실행")

