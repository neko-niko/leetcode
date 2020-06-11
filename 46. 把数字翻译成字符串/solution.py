import functools

class Solution:
    def translateNum(self, num: int) -> int:

        num_str = str(num)
        num_len = len(num_str)


        @functools.lru_cache()
        def inner_func(num_str: str, pos: int, num_len: int) -> int:
            if pos == num_len or pos == num_len - 1:
                return 1
            elif pos > num_len:
                return 0
            else:
                if num_str[pos] != "0" and int(num_str[pos: pos+2]) < 26:
                    return inner_func(num_str, pos+1, num_len) + inner_func(num_str, pos+2, num_len)

                return inner_func(num_str, pos+1, num_len)


        return inner_func(num_str, 0, num_len)


print(Solution().translateNum(506))