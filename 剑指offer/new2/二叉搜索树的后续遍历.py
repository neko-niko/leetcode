class Solution:
    def VerifySquenceOfBST(self, sequence):
        return self.judge(sequence, 0, len(sequence) - 1)

    def judge(self, lst: list, l, r):
        if l >= r:
            return True
        else:
            tmp = r
            print(tmp)
            midd = lst[-1]
            tmp -= 1
            print(tmp)
            print(midd)
            while lst[tmp] > midd:
                print('-')
                tmp -= 1
            if not all(map(lambda x: x < midd, lst[: r+1])):
                return False
            else:
                return (self.judge(lst, l, tmp) and self.judge(lst, tmp+1, r-1))

Solution().VerifySquenceOfBST(list(reversed(range(1, 6))))