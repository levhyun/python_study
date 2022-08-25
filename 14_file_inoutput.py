# 파일 입출력

file = open("testfile.txt", "w", encoding="utf8") # testfile.txt파일을 쓰기모드로 열기
print("test file", file=file)
file.write("a b c d e") # 파일에 입력
file.close() # 파일 닫기

file2 = open("testfile.txt", "r", encoding="utf8") # testfile.txt 읽기 모드로 열기
print("testfile.txt 내용:")
print(file2.read()) # 파일 안에 정보를 읽어 실행창에 출력
file2.close() # 파일 닫기

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