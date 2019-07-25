class Solution:
    def IsBalanced_Solution(self, pRoot):
        if self.IsBalanced_Solution2(pRoot) == -1:
            return False
        else:
            return True
    def IsBalanced_Solution2(self, pRoot):
        if not pRoot:
            return 0
        else:
            left = self.IsBalanced_Solution2(pRoot.left)
            right = self.IsBalanced_Solution2(pRoot.right)
            if left == -1 or right == -1:
                return -1
            else:
                return -1 if abs(left-right) > 1 else 1+max(left, right)