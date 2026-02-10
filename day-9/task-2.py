class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False


# Creating objects
mobile1 = Mobile("Samsung", "S23", 70000)
mobile2 = Mobile("Samsung", "S23", 75000)
mobile3 = Mobile("Apple", "iPhone 14", 80000)

# Comparing mobiles
print(mobile1 == mobile2)   # True (same brand & model)
print(mobile1 == mobile3)   # False (different brand & model)
print(mobile2 == mobile3)   # False
