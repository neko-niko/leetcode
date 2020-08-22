from typing import List
import itertools


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:

        add, mul, sub, div = range(4)

        def deep(vals: List[float]) -> bool:
            if not vals:
                return False
            if len(vals) == 1:
                return abs(vals[-1] - 24) < 1e-6

            for pos_x, x in enumerate(vals):
                for pos_y, y in enumerate(vals):
                    if pos_x != pos_y:
                        vals2 = []
                        for i, val in enumerate(vals):
                            if i != pos_x and i != pos_y:
                                vals2.append(val)

                        for opt in range(4):
                            if opt < 2 and pos_x > pos_y:
                                continue
                            if opt == add:
                                vals2.append(x + y)
                            elif opt == sub:
                                vals2.append(x - y)
                            elif opt == mul:
                                vals2.append(x * y)
                            else:
                                if y < 1e-9:
                                    continue
                                vals2.append(x / y)
                            if deep(vals2):
                                return True
                            vals2.pop()
            return False

        return deep(nums)

    # def judgePoint24(self, nums: List[int]) -> bool:
    #
    #     nums_len = len(nums)
    #     operat = ["+", "-", "*", "/"]
    #
    #     def deep(tmp: List, optl: List) -> bool:
    #         if len(tmp) == nums_len:
    #             val = tmp[0]
    #             for i in range(3):
    #                 opt = optl[i]
    #                 if opt == "+":
    #                     val += tmp[1 + i]
    #                 elif opt == "-":
    #                     val -= tmp[1 + i]
    #                 elif opt == "*":
    #                     val *= tmp[1 + i]
    #                 else:
    #                     val /= tmp[1 + i]
    #             if val > 0 and abs(val - 24) < 1:
    #                 return True
    #             return False
    #
    #         for i in range(len(tmp), nums_len):
    #             cur = nums[i]
    #             tmp2 = tmp + [cur]
    #             nums[len(tmp)], nums[i] = nums[i], nums[len(tmp)]
    #             flag = False
    #             if len(tmp2) > 1:
    #                 for opt in operat:
    #                     if not flag:
    #                         flag = deep(tmp2, optl + [opt])
    #
    #
    #             else:
    #                 flag = deep(tmp2, optl)
    #             nums[len(tmp)], nums[i] = nums[i], nums[len(tmp)]
    #
    #             if flag:
    #                 return True
    #         return False
    #
    #     return deep([], [])
    class Solution:
        def judgePoint24(self, nums: List[int]) -> bool:
            op = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y,
                  lambda x, y: x / y if y != 0 else float('inf')]
            for a, b, c, d in itertools.permutations(nums):
                for f, g, h in itertools.product(op, repeat=3):
                    if -1e-5 < f(g(h(a, b), c), d) - 24 < 1e-5 or \
                            -1e-5 < f(g(a, h(b, c)), d) - 24 < 1e-5 or \
                            -1e-5 < f(g(a, b), h(c, d)) - 24 < 1e-5 or \
                            -1e-5 < f(a, g(h(b, c), d)) - 24 < 1e-5 or \
                            -1e-5 < f(a, g(b, h(c, d))) - 24 < 1e-5:  # （这段if算一行
                        return True
            return False


print(Solution().judgePoint24([1, 2, 1, 2]))
