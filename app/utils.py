import os
from config import MEDIA_ROOT
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_media_path():
    return MEDIA_ROOT

def get_safe_filename(filename):
    """Генерирует безопасное имя файла"""
    name, ext = os.path.splitext(filename)
    return secure_filename(name) + ext.lower()