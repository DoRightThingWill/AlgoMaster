# leetcode link: https://leetcode.com/problems/trapping-rain-water/description/


# numbers = [0,1,0,2,1,0,1,3,2,1,2,1]
#                        | ^
#    index   0 1 2 3 4 5 6 7
#    water
# stack = [3]
# cur_idx = 7
# top_val = 1
# top_idx = 6
# h_diff = min(3,2 ) - top_val =  2 -1  = 0
# width = 1
# water = 1

# monotonic in this problem is not the most intuitive way
# two path to find the left_max and right_max is the most intuitive way

# TODO: tempalte for monotonic stack
# for index, num in enumerate(numbers):
#   while stack and monotonicity does not hold any more
#       process logic
#       stack.pop()
#   stack.append(index)
# TODO: The intuition of monotonic stack is: find the first min or max in one side

def trap(self, heights: List[int]) -> int:
    water_amount = 0
    stack = []

    for index, height in enumerate(heights):
        while stack and heights[stack[-1]] <= height:
            top_index = stack.pop()
            if not stack:
                break
            min_height = min(height, heights[stack[-1]])
            height_diff = min_height - heights[top_index]
            width = index - stack[-1] - 1
            cur_water = height_diff * width
            water_amount += cur_water

        stack.append(index)

    return water_amount