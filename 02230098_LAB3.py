#Part 1: Stack Implementation using Array
# Task1:Implementthe ArrayStack Class Structure
class ArrayStack:
    def __init__(self):
        self.capacity = 10
        self.stack = [None] * self.capacity  # array
        self.top = -1
        print("Created new ArrayStack with capacity:", self.capacity)

    # Check if stack is empty
    def is_empty(self):
        return self.top == -1

# Test
s = ArrayStack()
print("Stack is empty:", s.is_empty())

#Task2: Array-based Stack Operations (Python)
class ArrayStack:
    def __init__(self):
        self.capacity = 10
        self.stack = [None] * self.capacity
        self.top = -1
        print("Created new ArrayStack with capacity:", self.capacity)

    # Push
    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = element
            print(f"Pushed {element} to the stack")

    # Pop
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            element = self.stack[self.top]
            self.top -= 1
            print(f"Popped element: {element}")
            return element

    # Peek
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[self.top])
            return self.stack[self.top]

    # is_empty
    def is_empty(self):
        return self.top == -1

    # Size
    def size(self):
        return self.top + 1

    # Display
    def display(self):
        if self.is_empty():
            print("Display stack: []")
        else:
            print("Display stack:", self.stack[:self.top + 1])


# Test
s = ArrayStack()

s.push(10)
s.display()

s.push(20)
s.display()

s.push(30)
s.display()

s.peek()
s.pop()

print("Stack size:", s.size())
s.display()

#Part2: Stack Implementation using LinkedList
#Task3: Implementat the Node and LinkedStack Class Structure
# Node class
class Node:
    def __init__(self, data):
        self.data = data      # store element
        self.next = None      # reference to next node


# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None       # head of the stack
        self.size = 0         # number of elements
        print("Created new LinkedStack")

    # Check if empty
    def is_empty(self):
        return self.top is None


# Test
s = LinkedStack()
print("Stack is empty:", s.is_empty())

#Task4: Implement Linked List-based Stack Operations
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0
        print("Created new LinkedStack")

    # Push
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"Pushed {element} to the stack")

    # Pop
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            removed = self.top.data
            self.top = self.top.next
            self._size -= 1
            print(f"Popped element: {removed}")
            return removed

    # Peek
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)
            return self.top.data

    # is_empty
    def is_empty(self):
        return self.top is None

    # Size
    def size(self):
        return self._size

    # Display (list format)
    def display(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        print("Display stack:", elements)

    # Display (linked format)
    def display_linked(self):
        current = self.top
        output = ""
        while current:
            output += str(current.data) + " -> "
            current = current.next
        output += "null"
        print("Current stack:", output)

# Test
s = LinkedStack()

s.push(10)
s.display()

s.push(20)
s.display()

s.push(30)
s.display()

s.peek()
s.pop()

s.display_linked()
print("Stack size:", s.size())