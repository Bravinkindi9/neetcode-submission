class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # always binary search over the SMALLER array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        total_left = (n + m + 1) // 2

        left, right = 0, n

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = total_left - cut1

            left1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            right1 = nums1[cut1] if cut1 < n else float('inf')
            left2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            right2 = nums2[cut2] if cut2 < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (n + m) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = cut1 - 1
            else:
                left = cut1 + 1