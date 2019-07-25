# 所有组合，不能重复

def Solution1(n):
    res = []
    n_len = len(n)
    n.sort()
    def helper(i, temp):
        res.append(temp)
        for j in range(i, n_len):
            if j > i and n[j - 1] == n[j]:
                continue
            else:
                helper(j+1, temp + [n[j]])

    helper(0, [])
    return res


print(Solution1([1, 3, 3]))

# // 全排列

def Solution2(n):
    res = []
    n_len = len(n)
    n.sort()
    visted = [0] * n_len
    def helper(temp):
        if len(temp) == n_len:
            res.append(temp)
        else:
            for i in range(n_len):
                if visted[i] or (i > 0 and n[i] == n[i-1] and not visted[i-1]):
                    continue
                visted[i] = 1
                helper(temp + [n[i]])
                visted[i] = 0
    helper([])
    return res

print(Solution2([3, 0, 3]))

# 数的和

def Solution3(n, target):


    def helper(i, target, temp):
        if target == 0:
            res.append(temp)
        elif target < 0:
            return
        else:
            for j in range(i, n_len):
                helper(j+1, target - n[j], temp + [n[j]])
    res = []

    n_len = len(n)
    helper(0, target, [])
    return res


print(Solution3([10,1,2,7,6,1,5], 8))



# 分割回文串

def Solution4(n: str):
    res = []
    n_len = len(n)

    def helper(i, temp):
        if i == n_len:
            res.append(temp)
        else:
            for j in range(i, n_len):
                if n[i: j+1] == n[i: j+1][: : -1]:
                    helper(j + 1, temp+ [n[i: j+1]])
    helper(0, [])
    return res
print(Solution4('asdqfqavdvsghjfk'))