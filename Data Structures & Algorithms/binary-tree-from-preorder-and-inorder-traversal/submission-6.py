# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0 

        def dfs(limit): #recursively build subtree until limit value
            #limit => mid = position of root in inorder, also tells num nodes in each subtree
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder): #no more nodes
                return None
            if inorder[inIdx] == limit: #subtree complete
                inIdx += 1
                return None
            
            root = TreeNode(preorder[preIdx])  #root is first value of preorder
            preIdx += 1
            #pass in inorder sublists
            root.left = dfs(root.val) #nodes < root appear before it in inorder
            root.right = dfs(limit) #use original limit to build right rubtree
            return root

        return dfs(float("inf"))
        