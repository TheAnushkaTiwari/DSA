# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        def heightOfTree(node):
            if node is None:
                return 0
            left_subtree_height= heightOfTree(node.left)
            right_subtree_height= heightOfTree(node.right)
            # The longest path through THIS node (in edges) is left_height + right_height
            self.max_diameter= max(self.max_diameter, left_subtree_height + right_subtree_height)
            return 1 + max(left_subtree_height, right_subtree_height)
        heightOfTree(root)
        return self.max_diameter