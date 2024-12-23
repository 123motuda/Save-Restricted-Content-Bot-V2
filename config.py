# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24891943"))
API_HASH = getenv("API_HASH", "8c43549f7b146a43b6cf39c431336ebc")
BOT_TOKEN = getenv("BOT_TOKEN", "8045911813:AAG7BWmSDr7602l4y2iTCK0AMB0M3HO6H4k")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://motuda1073:<db_password>@cluster0.dtuqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
