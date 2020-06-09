# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
class Solution:
    def reOrderArray(self, array):
        lst_len = len(array)
        if lst_len == 0:
            return array
        fnt_ptr = 0
        rea_ptr = lst_len - 1
        while fnt_ptr < rea_ptr:
            if self.judge_odd(array[fnt_ptr]):
                fnt_ptr += 1
            else:
                while not self.judge_odd(array[rea_ptr]):
                    rea_ptr -= 1
                    if rea_ptr <= fnt_ptr:
                        return array
                array[rea_ptr], array[fnt_ptr] = array[fnt_ptr], array[rea_ptr]
                rea_ptr -= 1
                fnt_ptr += 1
        return array


    def judge_odd(self, number):
        return number % 2 == 1

if __name__ == '__main__':
    arr = list(range(1, 8))
    print(Solution().reOrderArray(arr))
