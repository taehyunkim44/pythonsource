# 최대공약수
# 두 개 이상의 정수의 공통 약수 중에서 가장 큰 값


def gcd(a, b):
    i = min(a, b)

    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


if __name__ == "__main__":
    print(gcd(1, 5))
    print(gcd(3, 6))
    print(gcd(60, 24))
    print(gcd(81, 27))
