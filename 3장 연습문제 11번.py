def generate_substrings(s):
    n = len(s)
    substrings = []
    for i in range(n):
        if s[i] == 'A':  # "A"로 시작하는 위치를 찾음
            for j in range(i+1, n):
                if s[j] == 'B':  # 해당 "A" 이후에 "B"로 끝나는 위치를 찾음
                    substrings.append(s[i:j + 1])  # i부터 j까지의 부분 문자열을 추가
    return substrings

string = "ADBAAEDBA"
substrings = generate_substrings(string)
print(", ".join(substrings))
