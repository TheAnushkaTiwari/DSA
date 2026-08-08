# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(node):
            if node is None:
                return []
            return (inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right))
        traversal=inorder_traversal(root)
        counts={}
        for num in traversal:
            if num in counts:
                counts[num]+=1
            else:
                counts[num]=1
        if not counts:
            mode=[]
        else:
            max_freq=max(counts.values())
            mode=[num for num,freq in counts.items() if freq==max_freq]
        return mode
        
        