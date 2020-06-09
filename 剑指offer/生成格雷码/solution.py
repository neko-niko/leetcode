
def GetGary(n):
    gary = []
    if n == 1:
        gary.append('0')
        gary.append('1')
        return gary
    last_gary = GetGary(n-1)
    for i in range(len(last_gary)):
        gary.append('0' + last_gary[i])
    for i in reversed(range(len(last_gary))):
        gary.append('1' + last_gary[i])
    return gary


print(GetGary(2))
