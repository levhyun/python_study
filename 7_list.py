# 리스트

list = [1,2,3]
print(list)

list.append(4) # 리스트 제일 뒤에 4 추가
print(list)

list.extend([5,6]) # 리스트 제일 뒤에 5, 6 추가 (문자나 다른 변수의 리스트도 가능)
print(list)

list.insert(2,4) # 리스트 안에서 index 2번에 4를 넣고 원래있던 숫자와 뒤에있는 숫자들을 뒤로 한칸씩 옮긴다
print(list)

del list[0] # 리스트 값 삭제
print(list)

print(list.pop()) # 리스트에서 제일 뒤에 있는 값을 밖으로 내보낸후 내보낸 값 출력
print(list)

print(list.count(4)) # 리스트에서 4의 갯수 출력

list2 = [5,4,3,2,1]
list2.sort() # 리스트 오름차순으로 정렬
print(list2)
list2.reverse() # 리스트 뒤집기
print(list2)

list2.clear() # 리스트 안에 값 모두 삭제
print(list2)
