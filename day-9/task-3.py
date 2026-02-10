class User:
    def __new__(cls, name):
        print("Object is being created")
        return super(User, cls).__new__(cls)

    def __init__(self, name):
        print("Object is initialized")
        self.name = name


# Creating object
user1 = User("Lavanya")
