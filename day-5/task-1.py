class InstagramAccount:
    def __init__(self, account_name, password):
        # Public variable
        self.account_name = account_name
        
        # Protected variable
        self._private_reels = []
        
        # Private variable
        self.__archived_reels = []
        
        # Private password
        self.__password = password

    # 1. Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    # 2. Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("Access Denied! Only followers can view private reels")

    # 3. Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    # 4. Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # 5. Getter for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Wrong password"

    # 6. Setter to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password. Password not updated")


# -------------------------------
# Task Execution
# -------------------------------

# Create object
account = InstagramAccount("lavanya_insta", "1234")

# Add private reels
account.add_private_reel("Dance Reel")
account.add_private_reel("Travel Reel")

# Add archived reels
account.add_archived_reel("Old Birthday Reel")
account.add_archived_reel("College Memories Reel")

print("\n--- Display Private Reels (Follower) ---")
account.display_private_reels(True)

print("\n--- Display Private Reels (Non-Follower) ---")
account.display_private_reels(False)

print("\n--- Display Archived Reels (Wrong Password) ---")
account.display_archived_reels("0000")

print("\n--- Display Archived Reels (Correct Password) ---")
account.display_archived_reels("1234")

print("\n--- Getter Method Test ---")
print(account.get_archived_reels("1234"))

print("\n--- Update Password ---")
account.set_password("1234", "5678")

print("\n--- Display Archived Reels After Password Change ---")
account.display_archived_reels("5678")
