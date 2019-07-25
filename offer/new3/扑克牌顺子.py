class Solution:
    def IsContinuous(self, numbers):
        max_ = 0
        min_ = 1e9
        boom = 0
        ok = set()
        if len(numbers) == 0:
            return False
        for i in numbers:
            if i == 0:
                boom += 1
            else:
                if i in ok or i == max_ or i == min_:
                    return False
                else:
                    if i > max_:
                        max_ = i
                    if i < min_:
                        min_ = i
                    if i < max_ and i > min_:
                        ok.add(i)
        print(max_, min_)
        if max_ - min_ > len(numbers) - 1:
            return False
        for i in range(min_, max_):
            if i in ok:
                ok.remove(i)
        if len(ok) == 0 or len(ok) <= boom:
            return True
        else:
            return False

Solution().IsContinuous([1,3,2,6,4])