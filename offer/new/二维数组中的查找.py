# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
import datetime
class Solution:
    # array 二维列表
    def Find(self, target, array):
        while True:
            row = len(array)
            col = len(array[0])
            if col == 0 or row == 0:
                return False
            if col == 1 and row == 1:
                if array[0][0] == target:
                    return True
                else:
                    return False
            nn = array[0][col-1]
            if nn == target:
                return True
            elif nn <= target:
                array = array[1:]
            else:
                array = [x[0: row-2] for x in array]


if __name__ == '__main__':
    time1 = datetime.datetime.now()
    print(Solution().Find(7, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
    print(time1)
    print(datetime.datetime.now())


