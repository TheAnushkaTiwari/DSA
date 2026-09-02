# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorderTraversal(node):
            if node is None:
                return []
            return (inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right))
        def make_balanced_bst(nums):
            if not nums:
                return None
            mid=len(nums)//2
            node=TreeNode(nums[mid])
            node.left= make_balanced_bst(nums[:mid])
            node.right= make_balanced_bst(nums[mid+1:])
            return node
        nums=inorderTraversal(root)
        return make_balanced_bst(nums)

        
        