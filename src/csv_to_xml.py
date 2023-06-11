import csv
import os
import xml.etree.ElementTree as ET


def create_or_append_xml(file_name, x, y, w, h, text, xml_file_path):
    if os.path.exists(xml_file_path):
        xml_tree = ET.parse(xml_file_path)
        xml_root = xml_tree.getroot()
    else:
        xml_root = ET.Element('root')
    handwritten_part_element = xml_root.find('handwritten-part')
    if handwritten_part_element is None:
        handwritten_part_element = ET.SubElement(xml_root, 'handwritten-part')

    line_element = ET.SubElement(handwritten_part_element, 'line', id="id")
    word_element = ET.SubElement(line_element, 'word', text=text)
    cmp_element = ET.SubElement(word_element, 'cmp', x=x, y=y, width=w, height=h)

    xml_tree = ET.ElementTree(xml_root)
    xml_tree.write(xml_file_path)


def convert_csv_to_xml(csv_file_path, output_dir):
    with open(csv_file_path, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row

        for row in reader:
            if len(row) == 6:
                file_name, x, y, w, h, text = row
            else:
                continue

            xml_file_path = os.path.join(output_dir, f"{file_name.split('.', 1)[0]}.xml")
            create_or_append_xml(file_name, x, y, w, h, text, xml_file_path)
            print(f"XML file '{xml_file_path}' generated or updated.")


if __name__ == '__main__':
    csv_file_path = "../data/annotations/coordswords.csv"
    output_dir = "../data/annotations/gt"

    os.makedirs(output_dir, exist_ok=True)

    convert_csv_to_xml(csv_file_path, output_dir)

