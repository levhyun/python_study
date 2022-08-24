# 함수

#abs = 절댓값 함수
print(abs(-5)) # -5의 절댓값 = 5

#pow = 제곱 함수
print(pow(4,2)) # 4의 2승 or 4의 2제곱 = 4*4 = 16

#max = 최댓값 함수
print(max(5,12)) # 5와 12 중 최댓값 = 12

#min = 최소값 함수
print(min(5,12)) # 5와 12 중 최소값 = 5

#round = 반올림 함수
print(round(3.14)) # 3.14를 반올림 = 3
print(round(4.99)) # 4.99를 반올림 = 5

from math import * # math라이브러리

#floor = 내림 함수
print(floor(4.99)) # 4.99를 내림 = 4

#ceil = 올림 함수
print(ceil(3.14)) # 3.14를 올림 = 4

#sqrt = 제곱근 함수
print(sqrt(16)) # 16의 제곱근 = 4  / 4*4=16

from random import * # random 라이브러리

#random = 난수 함수 or 랜덤 함수
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성

# 정수난수 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성

#randrange = 범위지정 난수생성
print(randrange(1,20)) # 1 ~ 20 미만의 임의의 값 생성
print(randint(1,20)) # 1 ~ 20 이하의 임의의 값 생성

# 문자영 처리 함수
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

