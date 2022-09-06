class hellopackage:
    def out(self):
        print("HELLO")

if __name__ == "__main__":
    print("직접 호출")
    a = hellopackage()
    a.out()
else:
    print("외부 호출")