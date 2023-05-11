import re

telegram_username_pattern = re.compile("^@[a-zA-Z0-9_]{5,32}$")
