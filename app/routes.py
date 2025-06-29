from flask import Blueprint, send_file, request, render_template
import os
from .utils import allowed_file, get_media_path

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        file.save(os.path.join(get_media_path(), file.filename))
        return {'status': 'ok'}, 200
    return {'error': 'Invalid file'}, 400

@bp.route('/files/<filename>')
def download(filename):
    return send_file(os.path.join(get_media_path(), filename))

@bp.route('/preview/<filename>')
def preview(filename):
    # Реализация предпросмотра ниже
    ...
import mimetypes
from flask import Response

# Добавить в routes.py
@bp.route('/files')
def list_files():
    media_path = get_media_path()
    files = []
    for f in os.listdir(media_path):
        if os.path.isfile(os.path.join(media_path, f)):
            file_type = mimetypes.guess_type(f)[0] or 'unknown'
            files.append({
                'name': f,
                'type': file_type.split('/')[0]  # 'image', 'video' и т.д.
            })
    return {'files': files}