# 모듈2

from module_code3 import *
# module_code3 파일을 선언
# from module_code3 import a, b, c <- 이렇게 쓸 메소드를 지정선언도 가능

print("\na=그대로 / b=(+2) / c=(+4)")

a(input("a : "))  # module_code3 파일 안에 a 함수호출
b(input("b : "))  # module_code3 파일 안에 b 함수호출
c(input("c : "))  # module_code3 파일 안에 c 함수호출
