from os import getenv

# Instagram Cookies (Optional - Only if you need Instagram downloads)
INST_COOKIES = """
# Replace with actual Instagram cookies if needed (e.g., for private IG content)
"""

# YouTube Cookies (Optional - Only if you need private YT downloads)
YTUB_COOKIES = """
# Replace with actual YouTube cookies if needed
"""

# Required Credentials (From Your Data)
API_ID = int(getenv("API_ID", "23450120"))
API_HASH = getenv("API_HASH", "6c44585f8e2efd9a6b261efecdaaa150")
BOT_TOKEN = getenv("BOT_TOKEN", "7455015845:AAFgY62Unhe82p-L7_D8TdQirIfC2RQNw_A")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8128958358").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://damealorica:moitiere2A@saverbot.znrlqwc.mongodb.net/?retryWrites=true&w=majority&appName=SaverBot")
LOG_GROUP = getenv("LOG_GROUP", "-1002707663831")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002676263803"))

# Optional/Limit Settings
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "100000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")  # Leave empty or add a URL
AD_API = getenv("AD_API", "")  # Ad API key (if monetizing)
STRING = getenv("STRING", "")  # Pyrogram session string (for userbot mode)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)  # YouTube cookies (if needed)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)  # Instagram cookies (if needed)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # Legacy invite link joining
