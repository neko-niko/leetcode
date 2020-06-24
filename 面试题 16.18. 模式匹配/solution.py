class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:

        len_p = len(pattern)
        len_v = len(value)

        count_a = pattern.count("a")
        count_b = len_p - count_a

        if count_b > count_a:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if char == 'b' else 'b' for char in pattern)
        if not pattern:
            return len_v == 0
        if not value:
            return count_b == 0
        for len_a in range(len_v // count_a + 1):
            total_b = len_v - len_a * count_a
            if (total_b == 0 and count_b == 0) or (count_b != 0 and total_b % count_b == 0):
                len_b = 0 if count_b == 0 else total_b // count_b
                str_b, str_a = None, None
                ptr = 0
                for sub in pattern:
                    if sub == 'a':
                        if not str_a:
                            str_a = value[ptr: ptr + len_a]
                        if value[ptr: ptr + len_a] == str_a:
                            ptr += len_a
                        else:
                            break
                    else:
                        if not str_b:
                            str_b = value[ptr: ptr + len_b]
                        if value[ptr: ptr + len_b] == str_b:
                            ptr += len_b
                        else:
                            break

                if str_a != str_b and ptr == len_v:
                    return True
        return False


print(Solution().patternMatching("abba", "dogcatcatdo"))