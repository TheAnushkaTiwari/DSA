# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums=[]
        def inorderTraversal(node):
            if not node:
                return
            inorderTraversal(node.left)
            nums.append(node.val)
            inorderTraversal(node.right)
        inorderTraversal(root)
            
        def make_balanced_bst(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            node=TreeNode(nums[mid])
            node.left= make_balanced_bst(left,mid-1)
            node.right= make_balanced_bst(mid+1,right)
            return node
        return make_balanced_bst(0,len(nums)-1)

        
        