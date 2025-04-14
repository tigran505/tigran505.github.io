import os
import re

# Настройки
ROOT_DIR = "./content"  # Путь к папке с .md-файлами
IMG_FOLDER = "/images/"  # Путь, который будет вставляться в markdown

def replace_obsidian_embeds(md_text):
    # Заменим ![[image.png]] на ![image](/images/image.png)
    pattern = r'!\[\[([^\[\]]+?)\]\]'
    
    def replacer(match):
        filename = match.group(1)
        alt_text = os.path.splitext(filename)[0]
        return f"![{alt_text}]({IMG_FOLDER}{filename})"

    return re.sub(pattern, replacer, md_text)

def process_md_files():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = replace_obsidian_embeds(content)

                if new_content != content:
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Обновлён: {full_path}")

if __name__ == "__main__":
    process_md_files()