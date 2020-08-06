from typing import List


class TreeNode:
    def __init__(self):
        self.ch = [0] * 26
        self.pos = -1


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ord_a = ord('a')
        Tree = [TreeNode()]

        def isPalindrome(s: str, left: int, right: int) -> bool:
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))

        def insert(s: str, pos: int):
            root = 0
            for i in s:
                i_pos = Tree[root].ch[ord(i) - ord_a]
                if i_pos == 0:
                    Tree.append(TreeNode())
                    Tree[root].ch[ord(i) - ord_a] = len(Tree) - 1
                root = Tree[root].ch[ord(i) - ord_a]
            Tree[root].pos = pos

        def find(s: str) -> int:
            root = 0
            for i in s:
                ord_i = ord(i)
                if Tree[root].ch[ord_i - ord_a] == 0:
                    return -1
                root = Tree[root].ch[ord_i - ord_a]
            return Tree[root].pos

        for pos, word in enumerate(words):
            insert(word, pos)

        res = []
        for pos, word in enumerate(words):
            for i in range(0, len(word) + 1):
                if i and isPalindrome(word, 0, i-1):
                    left_pos = find(word[i:][::-1])
                    if left_pos != -1 and left_pos != pos:
                        res.append([left_pos, pos])
                if isPalindrome(word, i, len(word)-1):

                    right_pos = find(word[0: i][::-1])
                    if right_pos != -1 and right_pos != pos:
                        res.append([pos, right_pos])
        return res


print(Solution().palindromePairs(["a","abc","aba",""]))
