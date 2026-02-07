class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []  

    
    def display_title(self):
        print("Title:", self.title)

    def display_description(self):
        print("Description:", self.description)

    def display_creator(self):
        print("Creator:", self.creator_name)

    def display_location(self):
        print("Location:", self.location)

    def display_likes(self):
        print("Likes:", self.likes)

    def display_comments(self):
        if not self.comments:
            print("No comments yet")
        else:
            print("Comments:")
            for comment in self.comments:
                print("-", comment)

   
    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    
    def add_comment(self, comment):
        self.comments.append(comment)

    def delete_comment(self, comment):
        if comment in self.comments:
            self.comments.remove(comment)
        else:
            print("Comment not found")
reel1 = Instagram(
    "Dancing",
    "Dancing with friends",
    "Lavanya",
    "Hyderabad"
)

reel2 = Instagram(
    "Finance Minister Conference",
    "Conference with officials",
    "Rahul",
    "Delhi"
)


reel1.liked()
reel1.liked()
reel2.liked()


reel1.add_comment("Amazing dance 🔥")
reel1.add_comment("Loved it ❤️")
reel2.add_comment("Very informative")


reel1.display_creator()
reel1.display_location()
reel1.display_likes()
reel1.display_comments()

print()

reel2.display_creator()
reel2.display_location()
reel2.display_likes()
reel2.display_comments()


print("\nObject IDs:")
print(id(reel1))
print(id(reel2))
