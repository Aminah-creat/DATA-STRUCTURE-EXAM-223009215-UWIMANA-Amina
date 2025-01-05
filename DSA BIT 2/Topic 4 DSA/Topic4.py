class Node:
    def __init__(self, key, value):
        self.key = key  
        self.value = value  
        self.left = None
        self.right = None


class BST:
    def __init__(self, max_size):
        self.root = None
        self.max_size = max_size
        self.current_size = 0

    def insert(self, key, value):
        if self.current_size >= self.max_size:
            print("Cannot insert: Maximum size reached.")
            return False
        self.root = self._insert(self.root, key, value)
        self.current_size += 1
        return True

    def _insert(self, root, key, value):
        if root is None:
            return Node(key, value)
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            print("Duplicate key. Ignored.")
        return root

    def search(self, key):
        """Search for a node by key."""
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        """Delete a node from the BST."""
        if self.search(key) is None:
            print("Key not found. Cannot delete.")
            return False
        self.root = self._delete(self.root, key)
        self.current_size -= 1
        return True

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: Get the inorder successor
            successor = self._min_value_node(root.right)
            root.key = successor.key
            root.value = successor.value
            root.right = self._delete(root.right, successor.key)
        return root

    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Inorder traversal of the BST."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append((root.key, root.value))
            self._inorder(root.right, result)

    def display(self):
        """Display the BST in an in-order traversal."""
        nodes = self.inorder()
        print("BST (Inorder Traversal):")
        for key, value in nodes:
            print(f"Key: {key}, Value: {value}")


# Example usage
if __name__ == "__main__":
    max_orders = 5
    bst = BST(max_orders)

    # Adding property listings
    bst.insert(3, "Order 3: Studio Apartment")
    bst.insert(1, "Order 1: 3-Bedroom Apartment")
    bst.insert(4, "Order 4: 4-Bedroom House")
    bst.insert(2, "Order 2: 2-Bedroom Condo")
    bst.insert(5, "Order 5: Luxury Villa")

    # Attempt to exceed the max size
    bst.insert(6, "Order 6: Penthouse")

    # Display all orders
    bst.display()

    # Search for a specific order
    key_to_search = 2
    found_node = bst.search(key_to_search)
    if found_node:
        print(f"Found: Key: {found_node.key}, Value: {found_node.value}")
    else:
        print(f"Order with key {key_to_search} not found.")

    # Delete an order
    bst.delete(3)
    
    print("After deleting order 3:")
    bst.insert(7, "Order 7: Comfort house")
    bst.display()
