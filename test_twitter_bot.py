from twitter_bot import post_tweet
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get credentials from environment variables
USERNAME = os.getenv('TWITTER_USERNAME')
PASSWORD = os.getenv('TWITTER_PASSWORD')

# Test message with emojis using Unicode 
TEST_MESSAGE = u"""Just wrapped up a productivity boost session!💡
I'm amazed at how much can be done in an hour with focus and the right tools. 📅

Heres my tip:
✅ Break tasks into small chunks
⏱️ Use timers to stay on track
🧘‍♂️ Take short breaks for mental clarity

Lets make today count! 🙌
#Focus"""


# Test the function
try:
    success = post_tweet(USERNAME, PASSWORD, TEST_MESSAGE)
    if success:
        print("Script completed successfully!")
    else:
        print("Script completed but tweet might not have been posted.")
except Exception as e:
    print(f"Error in main script: {e}")
