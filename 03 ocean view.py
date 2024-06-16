# leetcode link: https://leetcode.com/problems/buildings-with-an-ocean-view/

# TODO: monotonic stack holds numbers who does not have any number less than it in the right (left) side
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                top_index = stack.pop()
            stack.append(index)

        return stack

