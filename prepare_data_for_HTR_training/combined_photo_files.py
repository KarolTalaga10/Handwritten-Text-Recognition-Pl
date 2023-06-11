import os
import shutil

folder_names = ["2-FF", "3-FF", "4-FF", "5-FF"]
output_folder = "../data/dataset/img/FF/FF-FF/"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over the folder names
for folder_name in folder_names:
    folder_path = os.path.join("../data/", folder_name)
    scans_folder_path = os.path.join(folder_path, "scans")

    # Check if the 'scans' subfolder exists
    if os.path.exists(scans_folder_path) and os.path.isdir(scans_folder_path):
        # Iterate over the files in the 'scans' subfolder
        for filename in os.listdir(scans_folder_path):
            file_path = os.path.join(scans_folder_path, filename)
            if os.path.isfile(file_path):
                # Move the file to the combined folder
                output_path = os.path.join(output_folder, "FF-FF-" + filename)
                shutil.copy(file_path, output_path)
                print(f"Copied {filename} to {output_path}")

print("All photos combined successfully.")
