# 모듈

import module_code  # module_code 파일 선언

print("고기무한리필")
print("\n----가격----")
print("성인 : 13500원\n학생 : 10000원\n아기 : 5000원")

a = int(input("1.성인 / 2.학생 / 3.아기\n번호를 입력하세요. > "))
module_code.select(a)  # module_code 파일 안에 select 함수호출

import module_code2 as mc2  # module_code2 파일을 mc2로 대체 선언
a, b = input("ex)1+2 입력 > ").split("+")
mc2.plus(int(a),int(b))
