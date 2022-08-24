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


