def Function_Recall(a,b,c):
    print("\n1. 합을 구하기")
    print("2. 차을 구하기")
    num = int(input("\n번호를 입력하세요 > "))
    if num == 1:
        return a+b+c
    elif num == 2:
        return a-b-c
    else:
        pass

a=int(input("정수를 입력하세요. a : "))
b=int(input("정수를 입력하세요. b : "))
c=int(input("정수를 입력하세요. c : "))

print("결과 : %d" % Function_Recall(a,b,c))