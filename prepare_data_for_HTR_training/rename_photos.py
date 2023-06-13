from pathlib import Path
import os
from PIL import Image


def change_extension_folder(folder_path, new_extension):
    file_count = 0
    for filename in os.listdir(folder_path):
        if not filename.endswith(new_extension):
            file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.splitext(file_path)[0] + new_extension

            # Open the image
            image = Image.open(file_path)

            # Save the image with the new extension
            image.save(new_file_path)

            # Close the image
            image.close()

            # Delete the old file
            os.remove(file_path)
            file_count += 1
            print("Change file number: " + str(file_count))


# Example usage
if __name__ == '__main__':
    new_extension = ".png"
    directory_path = Path("../data/dataset/img/FF/FF-FF/")
    change_extension_folder(directory_path, new_extension)

