# 사전 함수

d = {1:"one",2:"two",3:"three","A":"a","B":"b"}

print(d[1]) # 실행결과 : one
print(d[2]) # 실행결과 : two
print(d.get(3)) # 실행결과 : three
print(d.get(14)) # 실행결과 : None

print(3 in d) # d안에 3이 있으면 True 출력하고 없으면 False

# 숫자 아니어도 문자도 가능
print(d["A"])

print(d["B"])
del d["B"]
print("B" in d)

print(d.keys()) # key 출력
print(d.values()) # values 출력
print(d.items()) # key, values 출력

d.clear() # 리스트 삭제
print(d)