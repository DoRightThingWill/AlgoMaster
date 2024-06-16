# leetcode link: https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row_heights = [0] * len(matrix[0])

        def get_max_rectangle_in_histogram(row, max_rectangle):

            for col in range(len(row_heights)):
                row_heights[col] = 0 if matrix[row][col] =="0" else row_heights[col] + 1
                stack = []
            max_rectangle = 0
            for index in range(len(row_heights) + 1):
                num = row_heights[index] if index != len(row_heights) else -1
                while stack and row_heights[stack[-1]] > num:
                    top_index = stack.pop()
                    height = row_heights[top_index]
                    left = stack[-1] if stack else -1
                    width = index - left -1
                    cur_rectangle = height * width
                    max_rectangle = max(max_rectangle, cur_rectangle)

                # when only two element left in the stack, the top element must be the smallest one in the array
                stack.append(index)

            return max_rectangle


        max_rectangle = float("-inf")
        for row in range(len(matrix)):
            cur_max = get_max_rectangle_in_histogram(row, max_rectangle)
            max_rectangle = max(cur_max, max_rectangle)

        return max_rectangle