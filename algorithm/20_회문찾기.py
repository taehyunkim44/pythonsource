# 스택(후입선출) : 삽입 1 2 3 4 -> 반출 4 3 2 1
# 큐(선입선출) : 삽입 1 2 3 4 -> 반출 1 2 3 4

# 리스트

# 회문찾기 : 순서대로 읽어도, 거꾸로 읽어도 내용이 같은 낱말이나 문장 찾기
# 역삼역, 기러기, 일요일, 사진사, 복불복, 토마토, ~
# mom, wow, level, radar, ~

# 주어진 문장이 회문인지 아닌지 찾기
# 회문이면 True, 아니면 False


def palindrome(s):
    qu = []  # Queue
    st = []  # Stack

    # 받은 문자를 queue와 stack에 넣기 (for)
    for c in s:
        if c.isalpha():
            qu.append(c.lower())
            st.append(c.lower())

    # 큐와 스택에 있는 문자 꺼내며 비교
    # 큐에 문자가 남아 있는 동안 반복
    while qu:
        # 큐와 스택에서 꺼낸 문자가 다르면 return false
        if qu.pop(0) != st.pop():
            return False  # pop(): 마지막 인덱스 기준 반환, pop(번호) 번호 인덱스 기준 반환
    # 루프 종료 후 True
    return True


# 문장의 앞뒤를 차례로 비교 (큐, 스택 없이)
def palindrome2(s):
    # 시작 위치
    start = 0

    # 종료 위치
    end = len(s) - 1

    while start < end:
        # start 위치에 있는 문자가 알파벳 문자가 아니면 start + 1
        if not s[start].isalpha():
            start += 1

        # end 위치에 있는 문자가 알파벳 문자가 아니면 end -1
        elif not s[end].isalpha():
            end -= 1

        # start와 end 위치에 있는 문자를 소문자로 변경한 후 비교해서 같지 않으면 False 리턴
        elif s[start].lower() != s[end].lower():
            return False

        # 위 세가지 경우가 아니면 start + 1, end - 1
        else:
            start += 1
            end -= 1

    # 반복문 종료 후 True 리턴
    return True


if __name__ == "__main__":
    print(palindrome("Wow"))
    print(palindrome("Madam, I'm Adam."))
    print(palindrome("Madam, I am Adam."))
    print()
    print(palindrome2("Wow"))
    print(palindrome2("Madam, I'm Adam."))
    print(palindrome2("Madam, I am Adam."))
