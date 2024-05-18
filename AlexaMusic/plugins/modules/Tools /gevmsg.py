
#Certainly! Below is the modified script to include a "Good Evening" command that sends a sticker along with a tea emoji:

python
Copy code
import random
from pyrogram import filters
from AlexaMusic import app

# Good Evening
@app.on_message(filters.command(["ood evening", "oodu Eveningu", "ood evening"], prefixes=["/", "g", "G", ""]))
def good_evening_command_handler(_, message):
    sender = message.from_user.mention
    tea_emoji = "🍵"
    sticker_id = "your_good_evening_sticker_id_here"  # Replace with your sticker ID
    app.send_sticker(message.chat.id, sticker_id)
    message.reply_text(f"**Goodu Eveningu, {sender}! Nalla t-time ho. {tea_emoji}**")

def get_random_video():
    videos = [
        "https://telegra.ph/file/2c63e594336bfab096835.mp4",  # video 1
        "https://telegra.ph/file/8e5a08a654079fef23659.mp4",  # video 2
        "https://telegra.ph/file/7dd498fb3c0ddd6c17e84.mp4",  # video 3
        "https://telegra.ph/file/941f1237d433974398b12.mp4",
    ]
    return random.choice(videos)


def get_random_emoji():
    emojis = [
        "🥰",
        "🥱",
        "🤗",
        "⭐",
    ]
    return random.choice(emojis)
