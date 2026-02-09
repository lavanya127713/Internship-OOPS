# Decorator definition
def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper


# Applying decorator
@admin_only
def dashboard(username):
    print("Welcome to Admin Dashboard")

dashboard("admin")
dashboard("user123")
