class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Added: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        item = self.stack.pop()
        print(f"Removed: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Current Stack:", self.stack)


# Examples
if __name__ == "__main__":
    # Create a new stack
    property_stack = Stack()

    # Simulating adding property listings
    property_stack.push("Property 1: 3-Bedroom Apartment")
    property_stack.push("Property 2: 4-Bedroom House")
    property_stack.push("Property 3: Studio Apartment")

    # Display the stack
    property_stack.display()

    # Peek at the top property
    print("Top property:", property_stack.peek())

    # Pop a property listing
    property_stack.pop()

    # Display the updated stack
    property_stack.display()
