### 사칙연산 함수 정의
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == "__main__":

    ### 사용자 입력
    while True:
        try:
            print("\n첫번째 숫자를 입력하세요.")
            input1 = float(input("입력: "))
            break
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    print("\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)")
    act = input("입력: ")

    while True:
        try:
            print("\n두번째 숫자를 입력하세요.")
            input2 = float(input("입력: "))
            break
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    ### 연산 수행
    if act == "+":
        result = plus(input1, input2)
    elif act == "-":
        result = minus(input1, input2)
    elif act == "*":
        result = mul(input1, input2)
    elif act == "/":
        result = divide(input1, input2)
    else:
        print("잘못된 연산 기호입니다. (+, -, *, / 중 하나를 입력하세요)")
        result = None

    if result is not None:
        print(f"사칙연산 결과는 {result}입니다.")
