# Part 1: Queue implementation using array
# Task 1: Implementthe ArrayQueue Class Structure
class ArrayQueue:
    def __init__(self):
        self.capacity = 10
        self.queue = [None] * self.capacity
        self.front = -1
        self.rear = -1

        print("Created new Queue with capacity:", self.capacity)

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def display_status(self):
        print("Queue is empty:", self.is_empty())


q = ArrayQueue()
q.display_status()

# Task 2: Implement Array-based Queue Operations
class Queue:
    def __init__(self):
        self.queue = []

    # 1. Enqueue
    def enqueue(self, element):
        self.queue.append(element)
        print(f"Enqueued {element} to the queue")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        removed = self.queue.pop(0)
        print(f"Dequeued element: {removed}")
        return removed

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Front element: {self.queue[0]}")
        return self.queue[0]

    # 4. Size
    def size(self):
        size = len(self.queue)
        print(f"Queue size: {size}")
        return size

    # 5. Display
    def display(self):
        print(f"Display queue: {self.queue}")

    def is_empty(self):
        return len(self.queue) == 0


# Example usage
q = Queue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

q.peek()

q.dequeue()

print(f"Current queue: {q.queue}")

q.size()

# Part 2: Queue implementation using Linked List
# Task 3: Implementthe Node and LinkedStack Class Structure
# Node class
class Node:
    def __init__(self, data):
        self.data = data   # Store element
        self.next = None   # Reference to next node


# LinkedQueue class
class LinkedQueue:
    def __init__(self):
        self.front = None   # First node
        self.rear = None    # Last node
        self.size = 0       # Number of elements
        print("Created new LinkedQueue")

    # Check if queue is empty
    def is_empty(self):
        empty = self.size == 0
        print(f"Queue is empty: {empty}")
        return empty


# Example usage
q = LinkedQueue()
q.is_empty()

# Task 4:
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedQueue class
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        print("Created new LinkedQueue")

    # 1. Enqueue
    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued {element} to the queue")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue becomes empty
            self.rear = None
        self._size -= 1
        print(f"Dequeued element: {removed}")
        return removed

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    # 4. is_empty
    def is_empty(self):
        return self._size == 0

    # 5. Size
    def size(self):
        print(f"Queue size: {self._size}")
        return self._size

    # 6. Display
    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Display queue: {elements}")

    # Extra: show linked format
    def display_linked(self):
        current = self.front
        result = ""
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "null"
        print(f"Current queue: {result}")


# Example usage
q = LinkedQueue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

q.peek()

q.dequeue()

q.display_linked()

q.size()