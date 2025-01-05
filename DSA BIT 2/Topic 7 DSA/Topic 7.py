def selection_sort(listings, key):
    """
    Sort property listings using Selection Sort based on a given key.
    :param listings: List of dictionaries representing property listings.
    :param key: The key in the dictionary to sort by.
    :return: Sorted list of listings.
    """
    n = len(listings)
    for i in range(n):
        # Find the index of the minimum element
        min_index = i
        for j in range(i + 1, n):
            if listings[j][key] < listings[min_index][key]:
                min_index = j

        # Swap the found minimum with the first element
        if min_index != i:
            listings[i], listings[min_index] = listings[min_index], listings[i]
            print(f"Swapped {listings[i]} with {listings[min_index]}")

    return listings


# Example usage
if __name__ == "__main__":
    # Sample property listings
    property_listings = [
        {"id": 1, "name": "Property A", "priority": 5},
        {"id": 2, "name": "Property B", "priority": 3},
        {"id": 3, "name": "Property C", "priority": 8},
        {"id": 4, "name": "Property D", "priority": 1},
    ]

    print("Original Listings:")
    for listing in property_listings:
        print(listing)

    # Sort listings by priority
    sorted_listings = selection_sort(property_listings, "priority")

    print("\nSorted Listings (by priority):")
    for listing in sorted_listings:
        print(listing)
