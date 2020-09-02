class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(' ')
        if not s or s[0] == 'e' or s[0] == 'E':
            return False

        ptr = 0
        s_len = len(s)

        while ptr < s_len and (s[ptr] == '-' or s[ptr] == '+'):
            ptr += 1
        if ptr > 1 or ptr == s_len:
            return False

        old_ptr = ptr
        while ptr < s_len and (s[ptr] >= '0' and s[ptr] <= '9'):
            ptr += 1
        prefix_is_num = ptr - old_ptr > 0

        if ptr == s_len and ptr > old_ptr:
            return True
        if s[ptr] != 'e' and s[ptr] != 'E' and s[ptr] != '.':
            return False

        if s[ptr] == '.':
            ptr += 1
            old_ptr = ptr
            while ptr < s_len and (s[ptr] >= '0' and s[ptr] <= '9'):
                ptr += 1
            if ptr == s_len:
                return prefix_is_num or ptr - old_ptr > 0
            if ptr > old_ptr:
                prefix_is_num = True

        if s[ptr] == 'e' or s[ptr] == 'E':
            ptr += 1
            old_ptr = ptr
            while ptr < s_len and (s[ptr] == '-' or s[ptr] == '+'):
                ptr += 1
            if ptr - old_ptr > 1:
                return False

            old_ptr = ptr
            while ptr < s_len and (s[ptr] >= '0' and s[ptr] <= '9'):
                ptr += 1
            if ptr == s_len and ptr > old_ptr:
                return prefix_is_num

        return False


print(Solution().isNumber(".2e81"))
