import csv
import os

folder_names = ["2-FF", "3-FF", "4-FF", "5-FF"]
output_folder = "../data/dataset/gt"
combined_output_file = "words.txt"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

combined_output_path = os.path.join(output_folder, combined_output_file)

# Clear the combined output file if it already exists
if os.path.exists(combined_output_path):
    open(combined_output_path, 'w').close()

for folder_name in folder_names:
    folder_path = os.path.join("../data/", folder_name)
    output_path = os.path.join(output_folder, f"{folder_name}_output.txt")

    # List all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith("Annotated.csv")]

    for csv_file in csv_files:
        csv_path = os.path.join(folder_path, csv_file)

        # Read the CSV file
        with open(csv_path, 'r', encoding="utf8") as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Extract the header and data rows from the CSV
        data_rows = rows[:]

        # Convert each data row to the desired format
        converted_rows = []
        for row in data_rows:
            filename = "FF-FF-" + row[0].replace(".jpg", ".png").replace(".jpeg", ".png").replace(".JPEG", ".png")\
                .replace(".JPG", ".png")
            data = row[1:]
            data.insert(0, 'ok')
            data.insert(1, '155')
            data.insert(6, 'A')
            converted_row = f"{filename} {' '.join(data)}"
            converted_rows.append(converted_row)

        # Append the converted rows to the combined output file
        with open(combined_output_path, 'a') as file:
            file.write('\n'.join(converted_rows) + '\n')


print(f"All conversions complete. Combined output file: {combined_output_path}")
