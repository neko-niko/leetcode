

class Solution:
    def solveNQueens(self, n: int) -> list:
        result = []
        self.recursive_core([], n, 0, result)
        result = self.graphical(result, n)
        return result


    def graphical(self, lst: list, n) -> list:
        result = []
        for i in lst:
            temp = []
            for j in i:
                row = [('Q' if k == j else '.') for k in range(n)]
                temp.append(''.join(row))
            result.append(temp)
        return result




    def recursive_core(self, lst: list, size, now, result: list):
        if now == size:
            lst1 = [i for i in lst]
            result.append(lst1)
            return
        else:
            for i in range(size):
                lst.append(i)
                if self.judge_core(lst, now):
                    self.recursive_core(lst, size, now+1, result)
                lst.pop()




    def judge_core(self, lst: list, now: int):
        if now == 0:
            return True

        cur_col = lst[now]
        cur_row = now
        for i in range(now):
            if (cur_col == lst[i]) or (abs(cur_row - i) == abs(cur_col - lst[i])):
                return False
        return True


if __name__ == '__main__':
    print(Solution().solveNQueens(4))