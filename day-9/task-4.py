class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Closed")


# Using with statement
with DatabaseConnection():
    print("Performing Query...")
