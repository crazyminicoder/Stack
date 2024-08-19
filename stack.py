class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
            return

        currentNode = self.top
        self.top = newNode
        self.top.next = currentNode

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        popped = self.top
        print('Top element:', popped.data)
        next = self.top.next
        self.top = None
        self.top = next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return

        print('Top element peek:', self.top.data)

    def size(self):
        if self.top is None:
            print('Stack is empty')
            return

        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next

        print("The size of the stack is: ", count)

    def clear(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        while temp:
            self.top = None
            self.top = temp.next
            temp = temp.next

    def printStack(self):
        if self.top is None:
            print("The stack is empty")
            return

        current = self.top
        while current:
            print(current.data, end='->' if current.next else '\n')
            current = current.next


st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)

st.printStack()

st.pop()

st.printStack()

st.peek()

st.size()


st.clear()

st.printStack()
