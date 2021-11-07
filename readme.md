## This Is Materials I Used for Coding Test Tutorial. Feel Free to Use if You Like

## For a BST, search v.s. traversal
* Traversal means you need to get ALL nodes of the tree.
* To find a value, though it looks like you are Traversing, you do not have to. You just need to choose to go left or right, by comparing the target value and the value of current node. Through this choosing, you skip LOTS OF nodes. 
* Considering the relationships of node, and child nodes in a BST, you either go left or right to search a target. Such searching in a BST does not need to cover ALL nodes. HOWEVER, for a general binary tree, no fixed comparison relationship between parent and children, to search a target, we need to go BOTH left and right, thus traversing all nodes is necessary.
* Overall, for a BST, you may not need trverall all nodes at all.
* The implementation is different as well
    * For traversal, as long as the left or right child node is not null or none, you could visit the corresponding subtree. Code looks like 
    ```python
    if cur_node.left != None:
        visit(cur_node.left)
    if cur_node.right != None:
        visit(cur_node.right)
    # these two conditions are not exclusive
    ```
    * For searching:
    ```python
    if target >= cur_node.value:
        search(cur_node.right, target)
    elif target < cur_node.right:
        search(cur_node.left, target)
    ```
* Searching in both recursive and iteration ways
    * Search--> recursive
    ```python
    # to find the exact target
    # if find it, return true; 
    # if the target not exist in the tree return false
    def search(tree, target):
        # the input tree is None
        # means we are at the tree END
        if tree == None:
            return False
        
        if tree.value == target:
            return True
        
        if target >= tree.value:
            return search(tree.right, target)
        else:
            return search(tree.left, target)
    ```
    * Search--> iteration
    ```python
    def search(tree, target):

        while tree != None:
            if tree.value == target:
                return True
            elif target >= tree.value:
                tree = tree.right
            else:
                tree = tree.left
        return False
    ```

* Traversal in both recursive and iteration ways
    * Recursive traversal--DFS
    ```python
    # in order traversal
    # this is depth-first-search
    def in_order_traverse(tree):
        # termination condition
        if tree == None:
            return
        
        # go to left child
        if tree.left != None:
            in_order_traverse(tree.left)
        # visit current node
        print(tree.value)
        # go to right child
        if tree.right != None:
            in_order_traverse(tree.right)
    ```
    * Iterative traversal---DFS
    ```python
    def dfs(tree):
        # handle the edge case when tree is None
        if tree == None:
            return
        # we need a stack to realize the DFS order
        node_stack = []
        # add the current node the stack (end of the list)
        node_stack.append(tree)

        while len(node_stack) !=0 :
            # pop out the tail node from the stack (list)
            cur_node = node_stack.pop()
            print(cur_node.value)
            if cur_node.left != None:
                node_stack.append(cur_node.left)
            if cur_node.right != None:
                node_stack.append(cur_node.right)

    ```
    * Iterative traversal---BFS
    ```python
    def dfs(tree):
        # here, we use a queue, rather than a stack to realize the order of BFS
        # handle the edge case when tree is None
        if tree == None:
            return
        # we need a queue to realize the BFS order
        node_queue = []
        # add the current node the queue (end of the list)
        node_queue.append(tree)

        while len(node_stack) !=0 :
            # pop out the head node from the queue (list)
            cur_node = node_queue.pop(0)
            print(cur_node.value)
            if cur_node.left != None:
                node_queue.append(cur_node.left)
            if cur_node.right != None:
                node_queue.append(cur_node.right)


## In a BST, Find the shortest path from Node A to Node B

* Given a root node, and target node, write a method return the path from the root node to the target node. This method could be built based on the search method.

    * path--> recursive
    ```python

    def path(tree, target):
 
        path = []
        return path_helper(tree, target, path)


    def path_helper(tree, target, path):
        # the input tree is None
        # means we are at the tree END and we did not find the target
        if tree == None:
            return None
        
        # if we find the target
        if tree.value == target:
            return path
        
        # if the current node is the target, we add this node to path
        path.append(tree)

        # then we move down to the child tree
        if target >= tree.value:
            return search(tree.right, target)
        else:
            return search(tree.left, target)


    ```
    * path--> iteration
    ```python
    def search(tree, target):

        path = []

        while tree != None:
            if tree.value == target:
                return path
            elif target >= tree.value:
                tree = tree.right
                path.append(tree)
            else:
                tree = tree.left
                path.append(tree)
        return None
    ```

    * Path problem is the variant of Searching problem
    * For iterative traversal, the stack is used to realize the order of the DFS. 
    * DFS-traversal, stack yes. Tree searching, stack No. Tree path, a list or stack is used for temporary storage of the visited node in the path.


## For a recursive method, when you need to return??
* If you only need to take some action, like print out a value, or replace a value, you do not need to return
* If you need the result from the sub-problem (next level recursion) to solve the upper level problem, you need a return.
* Most of the cases,  you need a return.

## Swap Items in a list
```python
# Generally, the syntax of python is simpler than Java
# in Python, code for switching items is pretty simple
list[start], list[end] = list[end], list[start]
# while in java, you need a temp item to store one item as a media
```
 ## for or while loop, you can avoid continue by ..
 ```python
while x < y:
    if a < b:
        counter = 0
    counter +=1
 
# code above is equivalent to 

while x < y:
    if a< b:
        counter = 1
        continue
    counter += 1
 ```