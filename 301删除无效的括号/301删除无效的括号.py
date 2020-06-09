# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
#
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
#
# 示例 1:
#
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
# 示例 2:
#
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
# 示例 3:
#
# 输入: ")("
# 输出: [""]

from typing import *


class Solution(object):

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """
    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        # If we have reached the end of string.
        if index == len(string):

            # If the current expression is valid. The only scenario where it can be
            # invalid here is if left > right. The other way around we handled early on in the recursion.
            if left_count == right_count:

                if rem_count <= self.min_removed:
                    # This is the resulting expression.
                    # Strings are immutable in Python so we move around a list in the recursion
                    # and eventually join to get the final string.
                    possible_ans = "".join(expr)

                    # If the current count of brackets removed < current minimum, ignore
                    # previous answers and update the current minimum count.
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)
        else:

            current_char = string[index]

            # If the current character is not a parenthesis, just recurse one step ahead.
            if current_char != '(' and  current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                # Else, one recursion is with ignoring the current character.
                # So, we increment the ignored counter and leave the left and right untouched.
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)

                expr.append(current_char)

                # If the current parenthesis is an opening bracket, we consider it
                # and increment left and  move forward
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)
                elif right_count < left_count:
                    # If the current parenthesis is a closing bracket, we consider it only if we
                    # have more number of opening brackets and increment right and move forward.
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)

                expr.pop()

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # Reset the class level variables that we use for every test case.
        self.reset()

        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)


class Solution2:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        min_rem = 1 << 63
        def helper(string: str, index: int, left, right, rem, temp:list):
            nonlocal res, min_rem
            if index == len(string):
                if left == right:
                    if rem <= min_rem:
                        if rem < min_rem:
                            res = set()
                            min_rem = rem
                        res.add(''.join(temp))
            else:
                cur_char = string[index]
                if cur_char != '(' and cur_char != ')':
                    temp.append(cur_char)
                    helper(string, index+1, left, right, rem, temp)
                    temp.pop()
                else:
                    helper(string, index+1, left, right, rem+1, temp)
                    temp.append(cur_char)
                    if cur_char == '(':
                        helper(string, index+1, left+1, right, rem, temp)
                    else:
                        if right < left:
                            helper(string, index+1, left, right+1, rem, temp)

                    temp.pop()
        # helper(s, 0, 0, 0, 0, [])
        res = set()

        def helper2(string: str, index, left_rem, right_rem, left_cot, right_cot, temp:list):
            nonlocal res
            if left_rem == 0 and right_rem == 0:
                res.add(''.join(temp) + string[index: ])
            elif index == len(string):
                return
            else:
                cur_char = string[index]
                if cur_char != '(' and cur_char != ')':
                    temp.append(cur_char)
                    helper2(string, index+1, left_rem, right_rem, left_cot, right_cot, temp)
                else:
                    if cur_char == '(':
                        if left_rem > 0:
                            helper2(string, index+1, left_rem -1, right_rem, left_cot, right_cot, temp)
                        temp.append(cur_char)
                        helper2(string, index+1, left_rem, right_rem, left_cot+1, right_cot, temp)
                    else:
                        if right_rem > 0:
                            helper2(string, index+1, left_rem, right_rem-1, left_cot, right_cot, temp)
                        temp.append(cur_char)
                        if left_cot > right_cot:
                            helper2(string, index+1, left_rem, right_rem, left_cot, right_cot+1, temp)
                temp.pop()
        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        helper2(s, 0, left, right, 0, 0, [])

        return list(res)
