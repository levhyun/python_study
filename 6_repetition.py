# 반복문 for while

list = ["1","2","3","4","5"]

for i in list:
    print(i, end=" ")

print("\n")

drink = "커피"
time = 5
while time >= 1:
    print("{0}준비까지 {1}초 남았습니다.".format(drink, time))
    time -= 1
    if time == 0:
        print("\n커피가 준비되었습니다!")
        break
    else:
        pass

# 한줄 for

students = [1,2,3,4,5]
print(students)
students = [i+1 for i in students]
print(students)

students_name = ["cg","yhs","ajx","e"]
students_name = [len(i) for i in students_name]
print(students_name)

# 슬라이싱

sl = "12345"
print("1~4번째 수 : " + sl[0:4])