class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """LIFO stack built from nodes, so it grows and shrinks dynamically."""

    def __init__(self):
        self.top = None

    def push(self, letter):
        node = Node(letter)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        letter = self.top.data
        self.top = self.top.next
        return letter

    def is_empty(self):
        return self.top is None

    def show(self):
        letters = []
        current = self.top
        while current is not None:
            letters.append(current.data)
            current = current.next
        return letters      # first item is the TOP of the stack


def main():
    last_name = input("Enter your last name: ").strip().upper() or "CADAMPOG"
    stack = Stack()

    print("\n--- PUSHING LETTERS ---")
    for letter in last_name:
        stack.push(letter)
        print(f"Pushed {letter} -> top to bottom: {stack.show()}")

    print("\n--- POPPING LETTERS ---")
    while not stack.is_empty():
        letter = stack.pop()
        print(f"Popped {letter} -> top to bottom: {stack.show()}")

    print("\nStack is empty.")


if __name__ == "__main__":
    main()