class Instagram:
    def create_post(self, content=None, post_type='photo'):
        """
        Create a new post on Instagram.

        Parameters:
        - content (str, list, or None): The content to post. It can be:
            - None: For text updates (e.g., quotes or status updates).
            - str: For a single photo or video with a caption.
            - list: For multiple photos or videos in a carousel post.
        - post_type (str): Type of post - 'photo', 'video', or 'reel'.

        Usage Examples:
        - create_post() → Text update
        - create_post("Beach vibes!", post_type='photo') → Single photo with caption
        - create_post(["pic1.jpg", "pic2.jpg"], post_type='carousel') → Multiple photos
        - create_post("funny_dance.mp4", post_type='reel') → A reel upload
        """
        if content is None:
            print("📝 Creating a text update...")
        
        elif isinstance(content, str):
            if post_type == 'photo':
                print(f"📸 Uploading a photo with caption: '{content}'")
            elif post_type == 'video':
                print(f"🎥 Uploading a video with description: '{content}'")
            elif post_type == 'reel':
                print(f"🎬 Uploading a Reel: '{content}'")
            else:
                print("⚠️ Unsupported post type. Choose 'photo', 'video', or 'reel'.")

        elif isinstance(content, list):
            if post_type == 'multiple':
                print(f"🖼️ Uploading a carousel with multiple items: {', '.join(content)}")
            else:
                print("⚠️ For multiple items, set post_type='multiple'.")

        else:
            print("❌ Unsupported content format. Please upload text, photo, video, or reel.")

# =======  Usage Examples =======
insta = Instagram()

insta.create_post()  # Text update
insta.create_post("Enjoying the sunset! 🌅")  # Single photo with caption
insta.create_post(["pic1.jpg", "pic2.jpg", "pic3.jpg"], post_type='multiple')  # Carousel post
insta.create_post("funny_dance.mp4", post_type='reel')  # Posting a Reel
insta.create_post("travel_video.mp4", post_type='video')  # Posting a Video

# Base class
class InstagramUser:
    def __init__(self, username):
        self.username = username

    def upload_post(self):
        print(f"{self.username} uploaded a basic post.")


# Subclass: Verified User
class VerifiedUser(InstagramUser):
    def upload_post(self):
        print(f"{self.username} (✔️ Verified) uploaded a post with insights and reach data.")


# Subclass: Business User
class BusinessUser(InstagramUser):
    def upload_post(self):
        print(f"{self.username} (Business) uploaded a post with promotion and ad options.")


# Subclass: Creator User
class CreatorUser(InstagramUser):
    def upload_post(self):
        print(f"{self.username} (Creator) uploaded a post with scheduling and audience targeting features.")




users = [
        VerifiedUser("celebrity_1"),
        BusinessUser("brand_store"),
        CreatorUser("content_creator"),
    ]

for user in users:
    user.upload_post()