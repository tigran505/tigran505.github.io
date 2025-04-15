import os
import re

IMAGE_FOLDER = "content/Кэш"
CONTENT_FOLDER = "content"

# 1. Переименование файлов с @ → _
def rename_images():
    renamed = {}
    for filename in os.listdir(IMAGE_FOLDER):
        if "@" in filename:
            new_name = filename.replace("@", "_")
            old_path = os.path.join(IMAGE_FOLDER, filename)
            new_path = os.path.join(IMAGE_FOLDER, new_name)
            os.rename(old_path, new_path)
            renamed[filename] = new_name
            print(f"🔁 {filename} → {new_name}")
    return renamed

# 2. Обновление ссылок в Markdown-файлах
def update_markdown_links(renamed_dict):
    for root, _, files in os.walk(CONTENT_FOLDER):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                original_content = content
                for old, new in renamed_dict.items():
                    pattern = re.escape(old)
                    content = re.sub(fr'!\[\[\s*{pattern}\s*\]\]', f"![[{new}]]", content)

                if content != original_content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"✅ Обновлён: {file_path}")

if __name__ == "__main__":
    renamed = rename_images()
    if renamed:
        update_markdown_links(renamed)
    else:
        print("👌 Нет файлов с '@', нечего менять.")