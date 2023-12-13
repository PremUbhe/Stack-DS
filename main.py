class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        self.head.next = self.head
        self.head = new_element

    def delete_first(self):
        self.head = self.head.next
        self.head.next = self.head.next.next


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, new_element):
        self.top = Node(new_element, self.top)

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

# Start setting up word1 Stack
stack = Stack()

# Test stack functionality
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.push(4)
print(stack.pop())
