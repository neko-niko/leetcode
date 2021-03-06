# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
# 归并排序
class Solution:
    def InversePairs(self, data):
        P = [0]
        lst = self.gbpx(data, P)
        return P[0] % 1000000007

    def gbpx(self, lst, P):
        if len(lst) <= 1:
            return lst
        else:
            left = self.gbpx(lst[0: len(lst) // 2], P)
            right = self.gbpx(lst[len(lst) // 2:], P)
            return self.core(left, right, P)

    def core(self, left, right, P):
        # print(1)
        l, r = 0, 0
        lst = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                lst.append(left[l])
                l += 1
            else:
                P[0] += len(left) - l
                lst.append(right[r])
                r += 1
        lst += left[l:]
        lst += right[r:]
        return lst

if __name__ == '__main__':
    s = Solution().InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575])
    print(s)