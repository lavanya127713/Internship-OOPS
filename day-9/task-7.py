class Session:
    def __del__(self):
        print("Session Ended")


# Creating object
obj = Session()

# Deleting object manually
del obj
