class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
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

    def iost(self, root):
        if root is None:
            return
        self.iost(root.left)
        self.stack.append(root.data)
        self.iost(root.right)
        return self.stack


res = Solution()
res.add(5)
res.add(3)
res.add(6)
res.add(2)
res.add(4)
res.add(8)
res.add(1)
res.add(7)
res.add(9)

print(res.iost(res.root))
ans = res.iost(res.root)

i = 1
while i < len(ans):
    ans.insert(i, 'null')
    i += 2

print(ans)
