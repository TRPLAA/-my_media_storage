import os
from config import MEDIA_ROOT

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_media_path():
    if not os.path.exists(MEDIA_ROOT):
        os.makedirs(MEDIA_ROOT)
    return MEDIA_ROOT