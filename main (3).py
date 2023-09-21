def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["apple", "banana", "apple", "orange", "apple", "grape"]
target_product = "apple"
result = linear_search_product(products, target_product)
print(result)