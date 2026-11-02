# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.preIdx = 0

        def dfs(l, r): #inorder range [l, r]
            if l > r:
                return None
            rootVal = preorder[self.preIdx] #root is first value of preorder
            self.preIdx += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal] #position of root in inorder, also tells num nodes in each subtree
            #pass in inorder sublists
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
        