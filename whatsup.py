# Base class
class Status:
    def __init__(self, username, text):
        self.username = username
        self.text = text

    def display(self):
        print(f"{self.username} posted a text status: {self.text}")


# Derived class for image status
class ImageStatus(Status):
    def __init__(self, username, text, image_path):
        super().__init__(username, text)
        self.image_path = image_path

    def display(self):
        print(f"{self.username} posted an image status: {self.text} [Image: {self.image_path}]")


# Derived class for video status
class VideoStatus(Status):
    def __init__(self, username, text, video_path):
        super().__init__(username, text)
        self.video_path = video_path

    def display(self):
        print(f"{self.username} posted a video status: {self.text} [Video: {self.video_path}]")


# Derived class for status with link and mention
class LinkMentionStatus(Status):
    def __init__(self, username, text, link, mention):
        super().__init__(username, text)
        self.link = link
        self.mention = mention

    def display(self):
        print(f"{self.username} posted a status: {self.text}")
        print(f"Includes link: {self.link}")
        print(f"Mentions: @{self.mention}")


# Derived class for status with like support
class LikeStatus(Status):
    def __init__(self, username, text):
        super().__init__(username, text)
        self.likes = 0
        self.reactions = []

    def like(self, user):
        self.likes += 1
        self.reactions.append(user)

    def display(self):
        print(f"{self.username} posted a status: {self.text}")
        print(f"Likes: {self.likes} | Reacted Users: {', '.join(self.reactions) if self.reactions else 'None'}")


# Demonstration
if __name__ == "__main__":
    s1 = Status("Alice", "Feeling happy today!")
    s2 = ImageStatus("Bob", "Look at this!", "photo.jpg")
    s3 = VideoStatus("Charlie", "Watch this video", "video.mp4")
    s4 = LinkMentionStatus("Diana", "Check this out!", "http://example.com", "Eve")
    s5 = LikeStatus("Eve", "New recipe uploaded!")

    # Simulating likes
    s5.like("Frank")
    s5.like("Grace")

    # Display all status updates
    for status in [s1, s2, s3, s4, s5]:
        status.display()
        print("-" * 50)