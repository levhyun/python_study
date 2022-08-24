file = open("testfile.txt", "w", encoding="utf8")
print("test file", file=file)
file.write("a b c d e")
file.close()

file2 = open("testfile.txt", "r", encoding="utf8")
print("testfile.txt 내용:")
print(file2.read())
file2.close()

file2 = open("testfile.txt", "r", encoding="utf8")
print("\n한줄 읽고 다음줄로 이동:")
print(file2.readline())
print("endline^")
print(file2.readline(), end="")
file2.close()

print("\n파일읽기 응용 ( while문 )")

file3 = open("testfile.txt", "r", encoding="utf8")
while True:
    line = file3.readline()
    if not line:
        break
    print(line, end="")
file3.close()