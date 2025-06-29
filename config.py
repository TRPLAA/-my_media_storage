import os
import tkinter as tk
from tkinter import filedialog
# Путь будет задан при установке

MEDIA_ROOT = os.path.join(os.path.expanduser("~"), "media_storage")
if not os.path.exists(MEDIA_ROOT):
    MEDIA_ROOT = filedialog.askdirectory(title="Select Storage Location")
    with open('config.py', 'w') as f:
        f.write(f"MEDIA_ROOT = r'{MEDIA_ROOT}'")

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

# Для разработки
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000
MAX_CONTENT_LENGTH = 10000 * 1024 * 1024  # 10000MB