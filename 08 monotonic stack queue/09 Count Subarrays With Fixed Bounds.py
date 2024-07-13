# In an array, looking for O(n) or O(logN) algo:
# two pointer
# sliding window
# greedy
# binary search
# monotonic stack or queue
# heap


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        last_out_of_boundary = -1
        current_min_index = -1
        current_max_index = -1

        for i, num in enumerate(nums):
            # num is out of boudary
            if num < minK or num > maxK:
                # reset pointers
                last_out_of_boundary = i
                # this means, the minK and maxK are not found
                current_min_index = -1
                current_max_index = -1
                continue

            # num is min or max
            if num == minK:
                current_min_index = i

            if num == maxK:
                current_max_index = i

            # num is within boundary
            if current_min_index != -1 and current_max_index != -1:
                valid_left_bound = min(current_min_index, current_max_index)
                count += valid_left_bound - last_out_of_boundary

        return count

