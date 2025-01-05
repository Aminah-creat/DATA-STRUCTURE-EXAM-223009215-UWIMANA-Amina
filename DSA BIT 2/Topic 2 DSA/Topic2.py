class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty!")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack:", self.stack)
# singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_start(self):
        if self.is_empty():
            print("List is empty!")
        else:
            self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            print("List is empty!")
        else:
            current = self.head
            while current.next and current.next.next:
                current = current.next
            current.next = None

    def display(self):
        if self.is_empty():
            print("List is empty!")
        else:
            current = self.head
            print("Property Listings:")
            while current:
                print(current.data)
                current = current.next
def main():
    # Stack for browsing history
    history_stack = Stack()

    # Singly Linked List for property listings
    property_list = SinglyLinkedList()

    # Sample Property Data
    property1 = {'id': 1, 'name': 'House 1', 'price': 500000}
    property2 = {'id': 2, 'name': 'House 2', 'price': 600000}
    property3 = {'id': 3, 'name': 'House 3', 'price': 700000}
    property4 = {'id': 4, 'name': 'House 4', 'price': 100000}

    # Add properties to the listing
    property_list.insert_at_end(property1)
    property_list.insert_at_end(property2)
    property_list.insert_at_end(property3)
    property_list.insert_at_end(property4)
   
    

    # Display current properties
    property_list.display()

    # Push the latest property to history stack
    history_stack.push(property3)

    # Show browsing history (most recent)
    print("Last viewed property:", history_stack.peek())

    # Let's say the user wants to go back to the last viewed property
    last_property = history_stack.pop()
    print("Going back to last viewed property:", last_property)

    # Remove the latest property from the list
    property_list.delete_at_end()

    # Display the updated properties
    print("Updated Property List:")
    property_list.display()

if __name__ == "__main__":
    main()

