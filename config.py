import os

# Путь будет задан при установке
MEDIA_ROOT = os.path.join(os.path.expanduser("~"), "media_storage")

# Для разработки
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000