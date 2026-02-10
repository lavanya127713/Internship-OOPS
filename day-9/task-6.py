class ShoppingCart:
    def __init__(self, items):
        self.items = items  # internal list

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


# Creating object
cart = ShoppingCart(["Apple", "Banana", "Milk"])

# Accessing item using index
print(cart[0])

# Updating item using index
cart[1] = "New Item"

print(cart.items)
