# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。


class MedianFinder:
    import heapq
    def __init__(self):
        self.cur_nums = 0
        self.min_ = []
        self.max_ = []

    def addNum(self, num: int) -> None:
        self.cur_nums += 1
        if self.cur_nums & 1:
            if self.max_:
                if num < self.max_[0][1]:
                    heapq.heappush(self.max_, (-num, num))
                    num = heapq.heappop(self.max_)[1]
            heapq.heappush(self.min_, num)
        else:
            if self.min_:
                if num > self.min_[0]:
                    heapq.heappush(self.min_, num)
                    num = heapq.heappop(self.min_)
            heapq.heappush(self.max_, (-num, num))

    def findMedian(self) -> float:
        if self.cur_nums & 1:
            return self.min_[0]
        else:
            return (self.max_[0][1] + self.min_[0]) / 2

if __name__ == '__main__':
    import heapq
    test = list(range(1, 10)) + list(range(100, 10, -1))
    heapq.heapify(test)
    print(test)