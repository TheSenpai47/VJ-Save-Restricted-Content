import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7333760658:AAHma51n_VYMCl9Gpt2Ak0sWTsx3GmkSgkw")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "15047947"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8e95af19215c497a2e8799ef7c6fa969")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rage47:rage@cluster0.9o1a1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
