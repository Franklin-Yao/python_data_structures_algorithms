from collections import Counter


class Solution:
    res = 0
    count = 0

    def helper(self, root, k):
        if root is None:
            return None
        self.helper(root.left, k)
        count -= 1
        if count == 0:
            res == root.val
        self.helper(root.right, k)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return None
        count = k
        res = 0
        self.helper(root, k)
        return res
S = "ABAACBAB"
T = "ABC"
res = minWindow(S, T)
print(res)