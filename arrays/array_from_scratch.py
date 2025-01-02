class array_from_scratch:
    def __init__(self, capacity=10):
        self.capacity = 10
        self.size = 0
        self.data = [None] * capacity
    
    def __str__(self):
        return str(self.data[i] for i in range(self.size))
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if index <= self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds.")
        
    def __setitem__(self, index, item):
        if index <= self.size:
            self.data[index] = item
        else:
            raise IndexError("Index out of bounds.")
        
    def __repr__(self):
        elements = [self.data[i] for i in range(0, self.size)]
        return f"Array({elements}, size={self.size}, capacity={self.capacity})"

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, item):
        if self.size == self.capacity :
            self._resize(2 * self.capacity)
        self.data[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty array.")
        
        element = self.data[self.size -1]
        self.data[self.size -1] = None
        self.size -= 1

        return element

    
    def insert(self, index, item):
        if not 0 <= index <= self.size:
            raise IndexError("Index out of range.")

        if index == self.size:
            self.append(item)
            return

        if self.size == self.capacity:
            self._resize(2*self.capacity)

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]

        self.data[index] = item
        self.size += 1

    def remove(self, index):
        if not 0 <= index <= self.size:
            raise IndexError("Index out of range.")
        
        for i in range(index, self.size -1):
            self.data[i] = self.data[i+1]
        self.data[self.size - 1] = None
        self.size -= 1