# leetcode link: https://leetcode.com/problems/sum-of-subarray-minimums/description/

# TODO: in the most typical monotonic stack, we iterate in range(n). Then the final stack is normally is not empty.
# If we iterate in range(n + 1) and when i == n + 1, we continue pop stack, we can pop all stack elements

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        sum = 0
        stack = []

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] > arr[i]):
                top_index = stack.pop()

                left = -1 if not stack else stack[-1]

            left_array_counts = top_index - left
            right_array_counts = i - top_index
            sub_array_counts = left_array_counts * right_array_counts
            sum += sub_array_counts * arr[top_index] % (10 ** 9 + 7)

        stack.append(i)

        return sum % (10 ** 9 + 7)