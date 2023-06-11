from pathlib import Path

directory_path = Path("../data/photos")

for file_path in directory_path.glob('*.jpg'):
    new_file_path = file_path.with_suffix('.png')
    file_path.rename(new_file_path)

for file_path in directory_path.glob('*.jpeg'):
    new_file_path = file_path.with_suffix('.png')
    file_path.rename(new_file_path)