class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_pre_order(self):
        result = []
        def dfs(node):
            if not node:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(self)
        print(result)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
