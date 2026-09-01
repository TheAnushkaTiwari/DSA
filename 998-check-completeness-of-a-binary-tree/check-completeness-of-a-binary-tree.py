# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check_tree(node):
            if node is None:
                return True, True, 0
            perfect_l, complete_l, height_l = check_tree(node.left)
            perfect_r, complete_r, height_r = check_tree(node.right)
            perfect= perfect_l and perfect_r and (height_l==height_r)
            #evaluate completeness
            if height_l==height_r:
                complete= perfect_l and complete_r
            elif height_l==height_r+1:
                complete= complete_l and perfect_r
            else:
                complete=False
            
            height= 1+ max(height_l, height_r)
            return perfect, complete, height

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        _, result, _ =check_tree(root)
        return result

        