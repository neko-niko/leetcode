from typing import *

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        visted = [[0 for j in i] for i in board]
        i_len = len(board)
        if i_len == 0:
            return []
        j_len = len(board[0])
        if j_len == 0:
            return []

        root = {}
        for word in words:
            sub = root
            for ch in word:
                sub = sub.setdefault(ch, {})
            sub['#'] = word
        # print(root)
        def helper(root: dict, i, j):
            # print(root, i, j)
            if '#' in root:
                res.append(root['#'])
                del root['#']
            # for key in root.keys():
            #     if i >= 0 and i < i_len and j >= 0 and j < j_len and not visted[i][j] and key == board[i][j]:
            #         visted[i][j] = 1
            #         helper(root[key], i+1, j)
            #         helper(root[key], i-1, j)
            #         helper(root[key], i, j+1)
            #         helper(root[key], i, j-1)
            #         visted[i][j] = 0
            if i >= 0 and i < i_len and j >= 0 and j < j_len and not visted[i][j] and board[i][j] in root:

                visted[i][j] = 1
                helper(root[board[i][j]], i+1, j)
                helper(root[board[i][j]], i-1, j)
                helper(root[board[i][j]], i, j+1)
                helper(root[board[i][j]], i, j-1)
                visted[i][j] = 0
        for i in range(i_len):
            for j in range(j_len):
                if board[i][j] in root:
                    helper(root, i, j)
        return res





borad = [["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]]
words = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
print(Solution().findWords(borad, words))