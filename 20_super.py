# super

class a():
    def __init__(self):
        print("a")

class b():
    def __init__(self):
        print("b")

class ab(a):
    def __init__(self):
        # a.__init__(self)
        super().__init__() # 위 코드 대신으로 super 명령어로 출력 가능

c = ab()

# 하지만 super은 다중 상속에서는 먼저 호출되는 하나만 출력

class ab(b,a):
    def __init__(self):
        super().__init__()

print("\n다중상속>")
d = ab()