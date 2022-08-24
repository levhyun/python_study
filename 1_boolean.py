# 기초출력

print("hello") # 출력명령어

# 심화 출력

print("a","b","c", sep=" vs ", end=" end\n")
# sep 는 문자와 문자사이에 동등하게 들어갈 것을 입력
# end 는 마지막에 들어갈 것을 입력

print("{0: >10}".format(500)) # 오른쪽 정렬, 10자리 공간 확보
print("{0: >+10}".format(500)) # 오른쪽 정렬, 10자리 공간 확보, 양수일땐 +, 음수일땐 -
print("{0:_<10}".format(500)) # 왼쪽 정렬, 10자리 공간 확보후 그자리에 _로 채우기
print("{0:,}".format(100000000000)) # 3자리 마다 콤마찍기

print("{0:.2f}".format(5/3)) # 소숫점 2번째 자리까지 출력

# 불린

print(True)
# True=참
print(False)
# False=거짓

# ex)
print(1==1) # 앞에 숫자와 뒤에 숫자는 같으므로 True

