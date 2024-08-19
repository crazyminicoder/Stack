class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def add(self, data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
            return

        currentNode = self.top
        self.top = newNode
        self.top.next = currentNode

    def printStack(self):
        if self.top is None:
            print("The stack is empty")
            return

        current = self.top
        while current:
            print(current.data, end='->' if current.next else '\n')
            current = current.next


st = Stack()
st.add(10)
st.add(20)
st.add(30)
st.add(40)
st.add(50)

st.printStack()
