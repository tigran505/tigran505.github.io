import os
import shutil
import yaml
import re

# Папки с заметками и картинками
SOURCE_DIR = "/Users/thinker/Documents/TigranWasSimplifed"
ARCHIVE_DIR = "/Users/thinker/Documents/TigranWasSimplifed/Архив"
DEST_CONTENT = "/Users/thinker/Desktop/quartz/content"
DEST_STATIC = "/Users/thinker/Desktop/quartz/quartz/static"

# Поддерживаемые расширения файлов
IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg"]

def should_publish(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        if not f.readline().startswith("---"):
            return False
        f.seek(0)
        try:
            frontmatter = []
            lines = f.readlines()
            if lines[0].strip() != "---":
                return False
            for line in lines[1:]:
                if line.strip() == "---":
                    break
                frontmatter.append(line)
            data = yaml.safe_load("".join(frontmatter))
            return data.get("publish", False)
        except Exception as e:
            print(f"Ошибка при разборе {file_path}: {e}")
            return False

def extract_image_paths(md_content):
    # Поиск Obsidian-стиля: ![[image.png]]
    obsidian_links = re.findall(r'!\[\[(.+?)\]\]', md_content)
    # Поиск Markdown-стиля: ![](path/image.png)
    markdown_links = re.findall(r'!\[.*?\]\((.+?)\)', md_content)
    return obsidian_links + markdown_links

def is_image(file):
    return any(file.lower().endswith(ext) for ext in IMAGE_EXTENSIONS)

def sync_notes_and_images():
    used_images = set()

    # Проходим по всем заметкам
    print("Поиск файлов .md в директории:", SOURCE_DIR)  # Логирование поиска файлов
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                print(f"Обрабатываем файл: {full_path}")  # Логируем обрабатываемые файлы
                if should_publish(full_path):
                    # Копируем заметку в content/
                    rel_path = os.path.relpath(full_path, SOURCE_DIR)
                    dest_path = os.path.join(DEST_CONTENT, rel_path)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(full_path, dest_path)

                    # Ищем картинки в заметке
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        images = extract_image_paths(content)
                        print(f"Найдено картинок в заметке {file}: {images}")  # Логируем найденные картинки
                        for img in images:
                            # Если путь картинки короткий, добавляем "Кэш/"
                            if not img.startswith("Кэш/"):
                                img = "Кэш/" + img
                            if is_image(img):
                                print(f"Найденная картинка: {img}")  # Для отладки
                                used_images.add(img)

    # Копируем найденные картинки в static/attachments
    print(f"Найдено {len(used_images)} картинок для копирования.")  # Логируем количество картинок
    for img_rel_path in used_images:
        img_source = os.path.join(ARCHIVE_DIR, img_rel_path)
        print(f"Пытаемся копировать картинку: {img_source}")  # Для отладки
        img_dest = os.path.join(DEST_STATIC, img_rel_path)
        if os.path.exists(img_source):
            os.makedirs(os.path.dirname(img_dest), exist_ok=True)
            shutil.copy2(img_source, img_dest)
        else:
            print(f"⚠️ Файл не найден: {img_source}")

if __name__ == "__main__":
    sync_notes_and_images()