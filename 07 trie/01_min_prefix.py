# leetcode 588
# https://leetcode.com/problems/design-in-memory-file-system/description/

# quick hints:
# in the structure of Trie, we do not define node.val
# the actual value is defined in parent node via {val:node} mapping
# path.split("/") needs to handle "" empty string specifically

import collections
class TrieNode:
    def __init__(self):
        # in the structure of Trie, we do not define node.val
        # the actual value is defined in parent node via {val:node} mapping
        self.children = collections.defaultdict(TrieNode)
        self.is_file = False
        self.content = ""


class FileSystem:

    def __init__(self):
        # no need new keyword in python to instantiate an object
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        # a/b/c
        # return c.chilren.keys().sort
        if path == "/":
            print(self.root.children.keys())
            return sorted(self.root.children.keys())

        # find the target trieNode
        cur_node = self.root
        for component in path.split("/"):
            if not component:
                continue
            cur_node = cur_node.children[component]

        if cur_node.is_file:
            return path.split("/")[-1]

        # else:
        return sorted(cur_node.children.keys())

    def mkdir(self, path: str) -> None:
        path_lst = path.split("/")
        node = self.root
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]
        print(self.root.children)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur_node = self.root
        for component in filePath.split("/"):
            if not component:
                continue
            if component not in cur_node.children:
                cur_node.children[component] = TrieNode()

            cur_node = cur_node.children[component]
        if not cur_node.is_file:
            cur_node.is_file = True

        cur_node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur_node = self.root
        for component in filePath.split("/"):
            if not component:
                continue
            cur_node = cur_node.children[component]

        return cur_node.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
