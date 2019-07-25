# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = list(s)
        s_len = len(s)
        if s_len == 0:
            return False
        cot = 0
        for i in s:
            if i == ' ':
                cot += 1
        replace_s = ['' for _ in range(s_len + cot*2)]
        s_ptr = s_len - 1
        r_ptr = len(replace_s) - 1
        while True:
            print(s_ptr)
            print(r_ptr)
            if s[s_ptr] == ' ':
                s_ptr -= 1
                replace_s[r_ptr] = '0'
                r_ptr -= 1
                replace_s[r_ptr] = '2'
                r_ptr -= 1
                replace_s[r_ptr] = '%'
                r_ptr -= 1
                if r_ptr == -1:
                    break
            else:
                replace_s[r_ptr] = s[s_ptr]
                r_ptr -= 1
                s_ptr -= 1
                if r_ptr == -1:
                    break
        return ''.join(replace_s)

if __name__ == '__main__':
    Solution().replaceSpace('')
