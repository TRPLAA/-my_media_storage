import sys
import os
from cx_Freeze import setup, Executable
import shutil

# Конфигурация сборки
build_exe_options = {
    "packages": ["flask", "jinja2"],
    "include_files": [
        ("app/templates", "templates"),
        ("config.py", "config.py")
    ]
}

# Настройка инсталлятора
setup(
    name="MediaStorage",
    version="1.0",
    description="Local Media Storage",
    options={"build_exe": build_exe_options},
    executables=[Executable("run.py", base=None)]
)

# Копирование медиа папки после сборки
def post_build():
    build_dir = "build"
    for dirpath, _, filenames in os.walk(build_dir):
        if "exe" in dirpath:
            target_dir = os.path.join(dirpath, "media")
            os.makedirs(target_dir, exist_ok=True)
            print(f"Created media folder at: {target_dir}")

if __name__ == "__main__":
    post_build()