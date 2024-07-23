class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays( nums2, nums1)
        
        m, n = len(nums1), len(nums2)

        low, high = 0, m

        while low <= high:
            cut_1 = (low + high) // 2
            cut_2 = (m + n + 1) // 2 - cut_1

            left_1 = float("-inf") if cut_1 == 0 else nums1[cut_1 -1]
            right_1 = float("inf") if cut_1 == m else nums1[cut_1]
            left_2 = float("-inf") if cut_2 == 0 else nums2[cut_2 - 1]
            right_2 = float("inf") if cut_2 == n else nums2[cut_2]

            if left_1 <= right_2 and left_2 <= right_1:
                # find the median
                if (m + n ) % 2 == 1 :
                    return max(left_1, left_2)
                else:
                    return (max(left_1, left_2) + min(right_1, right_2)) / 2
            elif left_1 > right_2:
                high = cut_1 - 1
            else:
                low = cut_1 + 1
        