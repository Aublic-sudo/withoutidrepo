import os

class Config(object):
    # Telegram Bot token
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # Telegram API credentials
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH")

    # Admin ID
    ADMIN_ID = int(os.environ.get("ADMIN_ID", 0))

    # MongoDB database URL
    DB_URL = os.environ.get("DB_URL")

    # Database name
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")

    # Log channels
    TXT_LOG = int(os.environ.get("TXT_LOG", 0))
    AUTH_LOG = int(os.environ.get("AUTH_LOG", 0))
    HIT_LOG = int(os.environ.get("HIT_LOG", 0))
    DRM_DUMP = int(os.environ.get("DRM_DUMP", 0))

    # Main channel
    CHANNEL = int(os.environ.get("CHANNEL", 0))

    # Links
    CH_URL = os.environ.get("CH_URL")
    OWNER = os.environ.get("OWNER")

    # Thumbnail
    THUMB_URL = os.environ.get("THUMB_URL")

    # API host
    HOST = os.environ.get("HOST")
