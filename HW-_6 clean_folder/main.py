import shutil
import sys
import scan
import normalize
from pathlib import Path

def handle_file(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok = True)
    new_name = normalize.normalize(path.stem) + path.suffix
    path.replace(target_folder/new_name)

def handle_archive(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok = True)

    normalized_name = normalize.normalize(path.stem)
    print(normalized_name)
    new_name = normalize.normalize(path.stem) + path.suffix
    print(new_name)

    archive_folder = root_folder/new_name

    try:
        shutil.unpack_archive(path, target_folder/normalized_name)
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()

def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass

def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass

def main(folder_path):
    scan.scan(folder_path)

    for file in scan.images_files:
        handle_file(file, folder_path, "Images")

    for file in scan.videos_files:
        handle_file(file, folder_path, "Videos")

    for file in scan.documents_files:
        handle_file(file, folder_path, "Documents")

    for file in scan.audio_files:
        handle_file(file, folder_path, "Audio")
    
    for file in scan.others:
        handle_file(file, folder_path, "Others")
    
    for file in scan.archives:
        handle_archive(file, folder_path, "Archives")

    get_folder_objects(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    main(arg)

