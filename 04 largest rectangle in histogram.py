# leetcod link: https://leetcode.com/problems/largest-rectangle-in-histogram/editorial/

# TODO: The O(n ^ 3) solution is easy to find. The intuition of monotonic solution is very similar with"
# find the sub-array who has the largest sum.
# With the current column in, what is the biggest rectangle.

def find_biggest_rectangle(numbers):
    stack = []
    max_rectangle = 0
    for index in range(len(numbers) + 1):
        num = numbers[index] if index != len(numbers) else -1
        while stack and numbers[stack[-1]] > num:
            top_index = stack.pop()
            height = numbers[top_index]
            left = stack[-1] if stack else -1
            width = index - left -1
            cur_rectangle = height * width
            max_rectangle = max(max_rectangle, cur_rectangle)

        # when only two element left in the stack, the top element must be the smallest one in the array
        stack.append(index)

    return max_rectangle