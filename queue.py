class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """FIFO queue built from nodes, so it grows and shrinks dynamically."""

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, letter):
        node = Node(letter)
        if self.rear is None:           # queue was empty
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        letter = self.front.data
        self.front = self.front.next
        if self.front is None:          # queue became empty
            self.rear = None
        return letter

    def is_empty(self):
        return self.front is None

    def show(self):
        letters = []
        current = self.front
        while current is not None:
            letters.append(current.data)
            current = current.next
        return letters      # first item is the FRONT of the queue


def main():
    last_name = input("Enter your last name: ").strip().upper() or "CADAMPOG"
    queue = Queue()

    print("\n--- ENQUEUING LETTERS ---")
    for letter in last_name:
        queue.enqueue(letter)
        print(f"Enqueued {letter} -> front to rear: {queue.show()}")

    print("\n--- DEQUEUING LETTERS ---")
    while not queue.is_empty():
        letter = queue.dequeue()
        print(f"Dequeued {letter} -> front to rear: {queue.show()}")

    print("\nQueue is empty.")


if __name__ == "__main__":
    main()