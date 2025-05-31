class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")
            if n <= 0:
                raise IndexError("Index must be a positive integer (1-based).")
            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node at index {n}: {deleted_data}")
                return
            current = self.head
            prev = None
            count = 1
            while current and count < n:
                prev = current
                current = current.next
                count += 1
            if not current:
                raise IndexError("Index out of range.")
            prev.next = current.next
            print(f"Deleted node at index {n}: {current.data}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    ll = LinkedList()
    print("Adding nodes:")
    for val in [10, 20, 30, 40, 50]:
        ll.add_node(val)

    print("\nOriginal list:")
    ll.print_list()

    print("\nDeleting 3rd node:")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nAttempting to delete 10th node (out of range):")
    ll.delete_nth_node(10)

    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nDeleting all remaining nodes:")
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    print("\nTry deleting from empty list:")
    ll.delete_nth_node(1)
