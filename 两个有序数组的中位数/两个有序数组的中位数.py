class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1

        imin, imax, help = 0, len1, (len1 + len2 + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = help - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < len1 and nums2[j - 1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:
                    left_num = nums2[j-1]
                elif j == 0:
                    left_num = nums1[i-1]
                else:
                    left_num = max(nums1[i-1], nums2[j-1])

                if ((len2 + len1) % 2) == 1:
                    return left_num

                if i == len1:
                    right_num = nums2[j]
                elif j == len2:
                    right_num = nums1[i]
                else:
                    right_num = min(nums1[i], nums2[j])

                return (right_num + left_num) / 2

























class Solution2:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        len1, len2 = len(nums1), len(nums2)

        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1


        imin, imax, help_ = 0, len1, (len1 + len2 + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = help_ - i
            if i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            elif i < len1 and nums2[j-1] > nums1[i]:
                imin = i + 1
            else:

                if i == 0:
                    left_num = nums2[j-1]
                elif j == 0:
                    left_num = nums1[i-1]
                else:
                    left_num = max(nums1[i-1], nums2[j-1])

                if ((len1 + len2) % 2) == 1:
                    return left_num

                if i == len1:
                    right_num = nums2[j]
                elif j == len2:
                    right_num = nums1[i]
                else:
                    right_num = min(nums1[i], nums2[j])
                return (left_num + right_num) / 2


