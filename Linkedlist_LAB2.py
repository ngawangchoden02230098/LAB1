# Task1
class CustomList:
    def __init__(self, capacity=10):
        # private array to store elements
        self._data = [None] * capacity
        
        # variables to track capacity and current size
        self._capacity = capacity
        self._size = 0
        
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")

   # Task2

    # 1. Append element
    def append(self, element):
        if self._size < self._capacity:
            self._data[self._size] = element
            self._size += 1
            print(f"Appended {element} to the list")
        else:
            print("List is full")

    # 2. Get element
    def get(self, index):
        if 0 <= index < self._size:
            print(f"Element at index {index}: {self._data[index]}")
            return self._data[index]
        else:
            print("Index out of range")

    # 3. Set element
    def set(self, index, element):
        if 0 <= index < self._size:
            self._data[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of range")

    # 4. Size method
    def size(self):
        print(f"Current size: {self._size}")
        return self._size


# Example usage
my_list = CustomList()

my_list.append(5)
my_list.get(0)

my_list.set(0, 10)
my_list.get(0)

my_list.size()