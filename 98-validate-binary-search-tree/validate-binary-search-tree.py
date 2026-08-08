# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result=0
        def remove_none(node):
            return [x for x in node if x is not None]
        def is_bst(node):
            if node is None:
                return True, None, None
            is_bst_l, min_l, max_l = is_bst(node.left)
            is_bst_r, min_r, max_r = is_bst(node.right)
            is_bst_node= (is_bst_l and is_bst_r and (max_l is None or max_l<node.val) and (max_r is None or min_r>node.val))
            min_key=min(remove_none([min_l, node.val, min_r]))
            max_key=max(remove_none([max_l, node.val, max_r]))
            return is_bst_node, min_key, max_key
        result,min_val, max_val=is_bst(root)
        return result
        