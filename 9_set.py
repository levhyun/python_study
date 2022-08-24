# 집합 함수

java = {"a","b","c"}
python = set(["a","d"])

# 교집합 (and)
print(java & python) # java와 python 둘다 들어있는 값을 출력
print(java.intersection(python)) # java와 python에 둘다 들어있는 값을 출력

#합집합 (or)
print(java | python) # java와 python 둘중 하나라도 들어있는 값을 출력
print(java.union(python)) # java와 python 둘중 하나라도 들어있는 값을 출력

# 차집합 (-)
print(java - python) # java에만 들어있는 값을 출력
print(java.difference(python)) # java에만 들어있는 값을 출력

# set안에 값 추가 및 삭제
python.add("e") # set 안에 e 추가
print(python)

java.remove("a") # set 안에 a 삭제
print(java)



