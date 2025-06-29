from flask import Blueprint, send_file, request, render_template, jsonify
from .utils import allowed_file, get_media_path
from werkzeug.utils import secure_filename
import mimetypes
import os
import json

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {'error': 'No file part'}, 400
        
    file = request.files['file']
    if file.filename == '':
        return {'error': 'No selected file'}, 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(get_media_path(), filename))
        return {'status': 'ok', 'filename': filename}, 200
        
    return {'error': 'Invalid file type'}, 400

@bp.route('/files/<filename>')
def download(filename):
    return send_file(os.path.join(get_media_path(), filename))

@bp.route('/preview/<filename>')
def preview_file(filename):
    media_path = get_media_path()
    filepath = os.path.join(media_path, filename)
    
    if not os.path.exists(filepath):
        return "File not found", 404
        
    file_type, _ = mimetypes.guess_type(filename)
    
    # Для изображений, видео и аудио используем встроенные теги
    if file_type:
        if file_type.startswith('image'):
            return f'<img src="/files/{filename}" style="max-width:100%">'
        elif file_type.startswith('video'):
            return f'<video controls src="/files/{filename}" style="max-width:100%"></video>'
        elif file_type.startswith('audio'):
            return f'<audio controls src="/files/{filename}"></audio>'
    
    # Для текстовых файлов
    if file_type and file_type.startswith('text'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return f'<pre>{content}</pre>'
        except:
            pass
    
    # Для неизвестных типов предлагаем скачать
    return f'''
        <h2>File Preview Not Available</h2>
        <p>File type cannot be previewed: {filename}</p>
        <a href="/files/{filename}" download>Download File</a>
    '''



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

@bp.route('/list-files')
def list_files():
    media_path = get_media_path()
    files = []
    for filename in os.listdir(media_path):
        filepath = os.path.join(media_path, filename)
        if os.path.isfile(filepath):
            file_type, _ = mimetypes.guess_type(filename)
            files.append({
                'name': filename,
                'type': file_type.split('/')[0] if file_type else 'unknown',
                'size': os.path.getsize(filepath)
            })
    return jsonify(files)