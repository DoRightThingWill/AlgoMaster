## This Is Materials I Used for Coding Test Tutorial. Feel Free to Use if You Like

## For a BST, search v.s. traversal
* Traversal means you need to get ALL nodes of the tree.
* To find a value, though it looks like you are Traversing, you do not have to. You just need to choose to go left or right, by comparing the target value and the value of current node. Through this choosing, you skip LOTS OF nodes. 
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
    
    * Iterative traversal---BFS

## For a recursive method, when you need to return??
* If you only need to take some action, like print out a value, or replace a value, you do not need to return
* If you need the result from the sub-problem (next level recursion) to solve the upper level problem, you need a return.
* Most of the cases,  you need a return.

