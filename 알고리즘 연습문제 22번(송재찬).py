# 사용자로부터 문자열을 입력받고 이것을 역순으로 출력하는 프로그램을 작성하라.
# 단, 스택 구조를 사용한다.

def reverse_string(input_string):
    stack = []  # 스택을 초기화합니다.

    # 문자열의 각 문자를 스택에 하나씩 넣습니다.
    for char in input_string:
        stack.append(char)

    reversed_string = ""  # 역순으로 된 문자열을 저장할 변수를 초기화합니다.

    # 스택에서 문자를 하나씩 빼면서 역순으로 된 문자열을 만듭니다.
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# 사용자로부터 문자열을 입력 받습니다.
input_string = input("문자열을 입력하세요: ")

# 역순으로 출력합니다.
print("입력한 문자열을 역순으로 출력합니다:", reverse_string(input_string))

# 스택은 한 방향으로만 입력하고 출력하게 되는 자료 구조임.
