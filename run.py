from app import create_app
from config import HOST, PORT, DEBUG, MAX_CONTENT_LENGTH

app = create_app()
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

if __name__ == "__main__":
    print(f"Server running at http://{HOST}:{PORT}")
    print(f"Media storage: {app.config.get('MEDIA_ROOT', '')}")
    app.run(host=HOST, port=PORT, debug=DEBUG)