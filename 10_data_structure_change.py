# 자료구조 변경

menu = {"커피","우유","주스"} # type : set
print(menu, type(menu))

menu = list(menu) # menu를 list type로 바꾼다
print(menu, type(menu))

menu = tuple(menu) # menu를 tuple type로 바꾼다
print(menu, type(menu))

menu = set(menu) # menu를 set type로 바꾼다
print(menu, type(menu))