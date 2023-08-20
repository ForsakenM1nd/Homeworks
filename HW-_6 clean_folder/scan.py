import sys
from pathlib import Path

# Перелік списків файлів, який включає задані рохширення
images_files = list()
videos_files = list()
documents_files = list()
audio_files = list()
archives = list()

others = list() # Файли без розширення та файли з невідомим розширенням
unknown = set() # Список невідомих розширень, які ми зустріли при сортуванні 
extentions = set() # Список відомих розширень, які ми зустріли при сортуванні 

EXTENSIONS_DICT = {
    'Images': ('.jpeg', '.png', '.jpg', '.svg', '.dng'),
    'Video': ('.avi', '.mp4', '.mov', '.mkv'),
    'Documents': ('.doc', '.docx', '.txt', '.xls', '.xlsx', '.djvu', '.rtf'),
    'Audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'Archives': ('.zip', '.gz', '.tar'),
}

registred_extensions = {
    "Images": images_files,
    "Videos": videos_files,
    "Documents": documents_files,
    "Audio": audio_files,
    "Archives": archives,
}

def get_extensions(file_name):
    return Path(file_name).suffix

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("Images", "Videos", "Documets", "Audio", "Other"):
                scan(item)
            continue

        extention = get_extensions(file_name=item.name)
        list_name = None
        new_name = folder/item.name

        if not extention:
            others.append(new_name)
        else:
            for key, values in EXTENSIONS_DICT.items():
                    if extention in values:
                        extentions.add(extention)
                        list_name = key
            
            try:
                container = registred_extensions[list_name]
                container.append(new_name)
            except KeyError:
                unknown.add(extention)
                others.append(new_name)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    scan(arg)

    print(f"Images: {images_files}\n")
    print(f"Videos: {videos_files}\n")
    print(f"Documents: {documents_files}\n")
    print(f"Audio: {audio_files}\n")
    print(f"Archives: {archives}\n")
     
    print(f"Unknown files: {others}\n")
    
    print(f"All known Extensions: {extentions}\n")
    print(f"Unknown extensions: {unknown}\n")