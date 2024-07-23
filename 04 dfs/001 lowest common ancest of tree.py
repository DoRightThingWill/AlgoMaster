# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # build node_parent_map
        node_parent_map = {}
        def build_parent_map(parent, cur_node, counter):

            if not cur_node:
                return
            
            node_parent_map[cur_node] = parent

            if cur_node.left:
                build_parent_map(cur_node, cur_node.left, counter)
            
            if cur_node.right:
                build_parent_map(cur_node, cur_node.right, counter)

        build_parent_map(None, root, 0)
        # build set of parent for p
        parent_set_of_p = set()
        parent_set_of_p.add(p)
        cur_node = p
        while cur_node:
            parent = node_parent_map[cur_node]
            parent_set_of_p.add(parent)
            cur_node = parent
        # backtrack ancester of q, the first ancester showing up in the parent_set_of_p is the target

        cur_node = q
        while cur_node:
            print(cur_node)
            if cur_node in parent_set_of_p:
                return cur_node

            cur_node = node_parent_map[cur_node]

            