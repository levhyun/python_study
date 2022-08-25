# 상속

class three(): # three라는 class를 선언후 method에 school변수를 지정
    def __init__(self, school):
        self.school = school

class two(): # two라는 class를 선언후 method에 birthday변수를 지정
    def __init__(self, birthday):
        self.birthday = birthday


class one(two, three): # one라는 class를 선언후 two, three class와 다중상속 후 method에 name, coding, birthday, school변수를 지정
    def __init__(self, name, coding, birthday, school):
        self.name = name
        self.coding = coding
        two.__init__(self, birthday) # two class 호출
        three.__init__(self, school) # three class 호출

        print("이름 : {0}".format(self.name))
        print("코딩 : {0}".format(self.coding))
        print("생일 : {0}".format(self.birthday))
        print("학교 : {0}".format(self.school))


name = input()
coding = input()
birthday = input()
school = input()

a = one(name, coding, birthday, school) # one class 호출 & 매개변수 값 전달
