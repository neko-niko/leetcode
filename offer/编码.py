
def Solution(String: str):
    str_len = len(String)
    cot = 0
    for i in range(str_len):
        nums = ord(String[i]) - ord('a')
        if i == 0:
            cot += (1 + 25 + 25*25 + 25*25*25) * nums
        elif i == 1:
            cot += ((1 + 25 + 25*25) * nums) + 1
        elif i == 2:
            cot += ((1 + 25) * nums) + 1
        else:
            cot += nums + 1
    print(cot)
    return cot

Solution('yahy')

