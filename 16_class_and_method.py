# 클래스와 메소드

class Class: # class 파일명
    def __init__(self, a, b, c): # 메소드 : def __init__(self, 변수)
        self.a = a
        self.b = b
        self.c = c
        print("{0} [{1}_{2}]\n".format(self.a, self.b, self.c)) # 받은 값 출력

one = Class("JAVA",1,3) # 클래스에 정보를 전달
two = Class("PYTHON",2,4) # 클래스에 정보를 전달
three = Class("MYSQL",5,7) # 클래스에 정보를 전달

class test:
    def __init__(self, d, e, f):
        self.d = d
        self.e = e
        self.f = f
        print("{0} : {1}-{2}".format(self.d,self.e,self.f))

t = test("test",6,7)
