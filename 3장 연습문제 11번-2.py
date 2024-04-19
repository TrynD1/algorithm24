def efficient_substrings(s):
    n = len(s)
    b_count = 0
    count = 0
    # 뒤에서부터 순회하여 B의 개수를 세면서 A를 만날 때마다 B의 개수를 더함
    for i in reversed(range(n)):
        if s[i] == 'B':
            b_count += 1
        elif s[i] == 'A':
            count += b_count
    return count

string = "ADBAAEDBA"
print(efficient_substrings(string))