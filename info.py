import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^-?\d+$')

def is_enabled(value, default):
    value = str(value).strip().lower()
    if value in ["true", "yes", "1", "enable", "y"]:
        return True
    if value in ["false", "no", "0", "disable", "n"]:
        return False
    return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '23800722'))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'True'), True)

PICS = environ.get('PICS', '').split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/aPc.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://graph.org/file/242b7f1b52743938d81f1.jpg')
FSUB_PICS = environ.get('FSUB_PICS', '').split()

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.fullmatch(admin) else admin for admin in environ.get('ADMINS', '5498521781').split()]
CHANNELS = [int(ch) if id_pattern.fullmatch(ch) else ch for ch in environ.get('CHANNELS', '').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '0'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '0'))
DEENDAYAL_MOVIE_UPDATE_CHANNEL = int(environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL', '0'))
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '0'))
auth_channel = environ.get('AUTH_CHANNEL', '0')
DELETE_CHANNELS = [int(dch) if id_pattern.fullmatch(dch) else dch for dch in environ.get('DELETE_CHANNELS', '').split()]
support_chat_id = environ.get('SUPPORT_CHAT_ID', '0')
reqst_channel = environ.get('REQST_CHANNEL_ID', '0')
AUTH_CHANNEL = [int(fch) if id_pattern.fullmatch(fch) else fch for fch in environ.get('AUTH_CHANNEL', '').split()]
MULTI_FSUB = [int(channel_id) for channel_id in environ.get('MULTI_FSUB', '').split() if id_pattern.fullmatch(channel_id)]

# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', '')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', '')

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', '')
DATABASE_URI2 = environ.get('DATABASE_URI2', '')
DATABASE_NAME = environ.get('DATABASE_NAME', 'imdb')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Deendayal_files')

# ============================
# Movie Notification & Update Settings
# ============================
DEENDAYAL_MOVIE_UPDATE_NOTIFICATION = is_enabled(environ.get('DEENDAYAL_MOVIE_UPDATE_NOTIFICATION', 'True'), True)
DEENDAYAL_IMAGE_FETCH = is_enabled(environ.get('DEENDAYAL_IMAGE_FETCH', 'True'), True)
CAPTION_LANGUAGES = ["Bhojpuri", "Hindi", "Bengali", "Tamil", "English", "Bangla", "Telugu", "Malayalam", "Kannada", "Marathi", "Punjabi", "Bengoli", "Gujrati", "Korean", "Gujarati", "Spanish", "French", "German", "Chinese", "Arabic", "Portuguese", "Russian", "Japanese", "Odia", "Assamese", "Urdu"]

# ============================
# Verification Settings
# ============================
VERIFY = is_enabled(environ.get('VERIFY', 'False'), False)
DEENDAYAL_VERIFY_EXPIRE = int(environ.get('DEENDAYAL_VERIFY_EXPIRE', 24))
DEENDAYAL_VERIFIED_LOG = int(environ.get('DEENDAYAL_VERIFIED_LOG', '0'))
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', '')

# ============================
# Link Shortener Configuration
# ============================
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', 'False'), False)
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnlinks.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', '')
IS_TUTORIAL = is_enabled(environ.get('IS_TUTORIAL', 'False'), False)

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', '')
CHNL_LNK = environ.get('CHNL_LNK', '')
OWNER_LNK = environ.get('OWNER_LNK', '')
DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK = environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK', '')
OWNERID = int(environ.get('OWNERID', '5498521781'))

# ============================
# User Configuration
# ============================
auth_users = [int(user) if id_pattern.fullmatch(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS.copy()
PREMIUM_USER = [int(user) if id_pattern.fullmatch(user) else user for user in environ.get('PREMIUM_USER', '').split()]

# ============================
# Miscellaneous Configuration
# ============================
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", 'True'), True)
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)
PORT = int(environ.get("PORT", "8080"))
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "False"), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
IMDBSEARCH_TEMPLATE = environ.get("IMDBSEARCH_TEMPLATE", f"{script.IMDBSEARCH_TEMPLATE}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split() if id_pattern.fullmatch(ch)]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "False"), False)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), True)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
PM_SEARCH = is_enabled(environ.get('PM_SEARCH', 'True'), True)
EMOJI_MODE = is_enabled(environ.get('EMOJI_MODE', 'True'), True)

# ============================
# Bot Configuration
# ============================
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL_ID = int(auth_channel) if auth_channel and id_pattern.fullmatch(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.fullmatch(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.fullmatch(support_chat_id) else None
LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]

# Keep the public/legacy name expected by existing plugins.
# The old source overwrote the list AUTH_CHANNEL with a scalar later.
AUTH_CHANNEL = AUTH_CHANNEL_ID

# ============================
# Server & Web Configuration
# ============================
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', 'False'), False)
NO_PORT = is_enabled(environ.get('NO_PORT', 'True'), True)
APP_NAME = environ.get('APP_NAME')
ON_HEROKU = 'DYNO' in environ
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME + '.herokuapp.com'
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'DeendayalBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'Deendayal'))
PING_INTERVAL = int(environ.get('PING_INTERVAL', '1200'))
HAS_SSL = is_enabled(environ.get('HAS_SSL', 'False'), False)
if HAS_SSL:
    URL = f"https://{FQDN}/"
elif NO_PORT:
    URL = f"http://{FQDN}/"
else:
    URL = f"http://{FQDN}:{PORT}/"

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# ============================
# Command admin
# ============================
commands = [
    """• /system - <code>sʏsᴛᴇᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</code>
• /del_msg - <code>ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏн...</code>
• /movie_update - <code>ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /pm_search - <code>ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs.</code>
• /chats - <code>ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs.</code>
• /leave - <code>ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable - <code>ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>""",
    """• /ban - <code>ʙᴀɴ ᴀ ᴜsᴇʀ.</code>
• /unban - <code>ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ.</code>
• /channel - <code>ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /gfilters - <code>ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜsᴇʀ.</code>""",
    """• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜsᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜsᴇʀ ғʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪsᴛ ᴏғ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴғᴏ ᴏғ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ.</code>
• /restart - <code>ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""
]

# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += "IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n"
LOG_STR += "P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n"
LOG_STR += "SINGLE_BUTTON is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled, filename and file size will be shown as different buttons.\n"
LOG_STR += f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n"
LOG_STR += "Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n"
LOG_STR += "Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n"
