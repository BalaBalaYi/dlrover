"""常见数结构"""
from multiprocessing.pool import worker

from test.tree.node import TreeNode, TrieNode

"""二叉查找树（BST）"""
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return

        # 依次查找空位
        node = self.root
        while node:
            if value < node.value:
                if not node.left:
                    node.left = TreeNode(value)
                    return
                node = node.left
            elif value > node.value:
                if not node.right:
                    node.right = TreeNode(value)
                    return
                node = node.right
            else:
                return

    def search(self, value):
        node = self.root
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node
        return None

    def delete(self, value):
        # 寻找要删除的节点及其父节点
        parent = None
        to_delete = self.root
        while to_delete and to_delete.val != value:
            parent = to_delete
            if value < to_delete.val:
                to_delete = to_delete.left
            else:
                to_delete = to_delete.right

        # 如果没有找到要删除的节点
        if not to_delete:
            return False

        # 如果找到，要进一步操作删除后的情况
        # 情况1：删除的节点有2个子节点
        if to_delete.left and to_delete.right:
            # 找到右子树的最小节点
            successor = to_delete.right
            successor_parent = to_delete

            # 继续向左寻找其最小值
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # 使用后继者的值替换当前节点的值
            to_delete.val = successor.val

            # 删除后继节点（它最多只有一个右子节点）
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        # 情况2：有0个或1个子节点
        child = to_delete.left if to_delete.left else to_delete.right
        if not parent:  # 删除的节点是根节点
            self.root = child
        elif parent.left == child:
            parent.left = child
        else:
            parent.right = child

        return True


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = TreeNode

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

    def delete(self, word):
        if not self.search(word):
            return False

        node = self.root
        stack = []

        # 找到单词的最后一个节点
        for char in word:
            stack.append((node, char))
            node = node.children[char]

        # 如果不是单词结尾，直接返回
        if not node.is_end:
            return False

        # 如果节点没有其他子节点，可以删除
        # 但如果需要保留前缀计数，则不删除节点
        while stack and not node.children and not node.is_end:
            parent, char = stack.pop()
            del parent.children[char]
            node = parent

        return True