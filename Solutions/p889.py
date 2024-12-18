class Solution:
    def constructFromPrePost(self, preorder, postorder):
        n = len(preorder)
        if n == 0:
            return None
        root = TreeNode(preorder[0])
        if n == 1:
            return root
        for i in range(n - 1):
            if postorder[i] == preorder[1]:
                root.left = self.constructFromPrePost(
                    preorder[1 : 1 + i + 1], postorder[: i + 1]
                )
                root.right = self.constructFromPrePost(
                    preorder[1 + i + 1 :], postorder[i + 1 : -1]
                )
                return root