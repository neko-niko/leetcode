from typing import *


class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        if len(buildings) == 0:
            return []
        elif len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        left = self.getSkyline(buildings[: len(buildings) // 2])
        right = self.getSkyline(buildings[len(buildings) // 2: ])
        return self.merge(left, right)

    def merge(self, left, right) -> List[List[int]]:
        l_n, r_n = len(left), len(right)
        l_p, r_p = 0, 0
        l_y, r_y, c_y = 0, 0, 0
        output = []
        def add_out(x, y):
            if not output or output[-1][0] != x:
                output.append([x, y])
            else:
                output[-1][1] =  y

        def last(c_y, lst, p):
            n = len(lst)
            while p < n:
                x, y = lst[p]
                if y != c_y:
                    add_out(x, y)
                p += 1


        while l_p < l_n and r_p < r_n:
            tl, tr = left[l_p], right[r_p]
            if tl[0] < tr[0]:
                x, l_y = tl
                l_p += 1
            else:
                x, r_y = tr
                r_p += 1
            max_y = max(l_y, r_y)
            if c_y != max_y:
                add_out(x, max_y)
                c_y = max_y
        last(c_y, left, l_p)
        last(c_y, right, r_p)
        return output












class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])

        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):

        def update_output(x, y):
            if not output or output[-1][0] != x:
                output.append([x, y])
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, curr_y):
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        p_l = p_r = 0
        curr_y = left_y = right_y = 0
        output = []

        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            max_y = max(left_y, right_y)
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        append_skyline(p_l, left, n_l, curr_y)

        append_skyline(p_r, right, n_r, curr_y)

        return output

