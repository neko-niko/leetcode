import sys

def solution(OString):
    OString = list(OString)
    re_str = list(reversed(OString))
    str_len = len(OString)
    i = 1
    matrix = [[0 for _ in range(str_len+1)] for i in range(str_len+1)]

    while i <= str_len:
        j = 1
        while j <= str_len:
            if OString[i-1] == re_str[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
            j += 1
        i += 1
    print(len(OString) - matrix[str_len][str_len])
    return matrix[str_len][str_len]

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        print(solution(line))