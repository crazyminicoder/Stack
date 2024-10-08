# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class inorder:
    def __init__(self):
        self.root = None
        self.stack = []

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            self._add(self.root, data)

    def _add(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._add(root.left, data)
        else:
            if data > root.data:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self._add(root.right, data)

    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.stack.append(root.data)

        self.inorderTraversal(root.right)

    def getStack(self):
        return self.stack


res = inorder()

res.add(1)
res.add(2)
res.add(3)
res.add(40)
res.add(25)
res.add(4)
res.add(14)
res.add(44)
res.add(9)
res.add(15)
res.add(11)
res.add(21)

res.inorderTraversal(res.root)

print(res.getStack())
