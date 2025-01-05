class TreeNode:
    """A node in the general tree."""
    def __init__(self, name, data=None):
        self.name = name  # Node name (e.g., City, Neighborhood, etc.)
        self.data = data  # Associated data (e.g., property details)
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        """Add a child to the current node."""
        self.children.append(child_node)
        print(f"Added child '{child_node.name}' under '{self.name}'.")

    def display(self, level=0):
        """Display the tree structure."""
        indent = " " * (level * 4)
        print(f"{indent}- {self.name}: {self.data}")
        for child in self.children:
            child.display(level + 1)


class PropertyTree:
    """Tree structure to manage property listings."""
    def __init__(self):
        self.root = TreeNode("Properties")  # Root of the tree

    def add_property(self, categories, property_details):
        """
        Add a property under specific categories.
        :param categories: List of categories (e.g., ["City", "Neighborhood", "Property Type"])
        :param property_details: Details of the property to add
        """
        current_node = self.root
        for category in categories:
            # Check if category exists among the current node's children
            child_node = next((child for child in current_node.children if child.name == category), None)
            if not child_node:
                # If the category doesn't exist, create a new child node
                child_node = TreeNode(category)
                current_node.add_child(child_node)
            current_node = child_node
        # Add the property details to the final category
        current_node.add_child(TreeNode(property_details))

    def display_tree(self):
        """Display the entire property tree."""
        self.root.display()


# Example usage
if __name__ == "__main__":
    property_tree = PropertyTree()

    # Add property listings
    property_tree.add_property(["City A", "Downtown", "Apartments"], "Property 1: 2-Bedroom Apartment")
    property_tree.add_property(["City A", "Downtown", "Apartments"], "Property 2: Studio Apartment")
    property_tree.add_property(["City A", "Uptown", "Houses"], "Property 3: 4-Bedroom House")
    property_tree.add_property(["City B", "Suburb", "Villas"], "Property 4: Luxury Villa")

    # Display the hierarchical tree
    print("Hierarchical Property Tree:")
    property_tree.display_tree()
