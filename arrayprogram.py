class DynamicArray:
    """An array that grows when full and shrinks when mostly empty."""

    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def add(self, letter):
        if self.size == self.capacity:        # full, so grow
            self._resize(self.capacity * 2)
        self.data[self.size] = letter
        self.size += 1

    def remove(self):
        if self.size == 0:
            return None
        self.size -= 1
        letter = self.data[self.size]
        self.data[self.size] = None
        if 0 < self.size <= self.capacity // 4:   # mostly empty, so shrink
            self._resize(self.capacity // 2)
        return letter

    def is_empty(self):
        return self.size == 0

    def show(self):
        return self.data[:self.size]


def main():
    last_name = input("Enter your last name: ").strip().upper() or "CADAMPOG"
    arr = DynamicArray()

    print("\n--- ADDING LETTERS ---")
    for letter in last_name:
        arr.add(letter)
        print(f"Added {letter}  -> {arr.show()}  (capacity: {arr.capacity})")

    print("\n--- REMOVING LETTERS ---")
    while not arr.is_empty():
        letter = arr.remove()
        print(f"Removed {letter} -> {arr.show()}  (capacity: {arr.capacity})")

    print("\nArray is empty.")


if __name__ == "__main__":
    main()