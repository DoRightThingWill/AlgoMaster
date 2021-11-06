## These Are Key Points about Coding Test. Be Sure to Distinguish the Key Difference

### For a BST, search v.s. traversal
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
    
    * Search--> iteration
* Traversal in both recursive and iteration ways
