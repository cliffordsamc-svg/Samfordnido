class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, letter):
        new_node = Node(letter)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:     # go to the last node
            current = current.next
        current.next = new_node

    def remove(self):
        if self.head is None:
            return None
        letter = self.head.data
        self.head = self.head.next          # remove from the head
        return letter

    def is_empty(self):
        return self.head is None

    def show(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        parts.append("NULL")
        return " -> ".join(parts)


def main():
    last_name = input("Enter your last name: ").strip().upper() or "CADAMPOG"
    linked_list = LinkedList()

    print("\n--- ADDING LETTERS ---")
    for letter in last_name:
        linked_list.add(letter)
        print(f"Added {letter}  : {linked_list.show()}")

    print("\n--- REMOVING LETTERS ---")
    while not linked_list.is_empty():
        letter = linked_list.remove()
        print(f"Removed {letter} : {linked_list.show()}")

    print("\nLinked list is empty.")


if __name__ == "__main__":
    main()