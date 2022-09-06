class byepackage:
    def out(self):
        print("BYE")

if __name__ == "__main__":
    print("직접 호출")
    a = byepackage()
    a.out()
else:
    print("외부 호출")