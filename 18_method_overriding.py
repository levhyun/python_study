# 메소드 오버라이딩

""" 정의
오버라이딩은 부모 클래스의 메소드를,
자식 클래스에서 재정의 하여 사용하는 것을 의미
"""

class o1():
    def __init__(self):
        self.over = 2

    def ov(self):
        return self.over


class o2(o1):
    def ov(self):  # 메소드 변경 => 메소드 오버라이딩
        return self.over * 4


a = o2()
print(a.ov())