# 사용자 정의 모듈

# def prt1(): 로 함수 정의
def prt1():
    print("이제 난 하루살이")


def prt2():
    print("하루 하루~~")


def prt3():
    print("내일도 잃어버린채~")


# 모듈이 잘만들어졌는지 테스트 할 때 사용하는 개념
if __name__ == "__main__":
    # print("prints")
    prt1()
    prt2()
    prt3()
