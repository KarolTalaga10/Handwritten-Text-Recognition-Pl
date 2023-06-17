import os
import shutil
import random

import cv2
from PIL import ImageDraw, Image, ImageFont
from matplotlib import pyplot as plt

import SimpleHTR.src.main
import WordDetectorNN.src.infer
import WordDetectorNN.src.dataloader

font_path = "../Arial_Unicode_MS_Font.ttf"


def interference():
    list_recognized = []
    temp_folder, imgs, aabbs = WordDetectorNN.src.infer.main(path_to_test_folder='../data/test')
    if temp_folder:
        list_recognized = SimpleHTR.src.main.main(temp_folder, True)
    else:
        raise FileExistsError
    print(list_recognized)
    end = 0
    img_no = 0
    for i, (img, aabb) in enumerate(zip(imgs, aabbs)):
        img = Image.fromarray(img)
        draw = ImageDraw.Draw(img)
        for j, ab in enumerate(aabb):
            color = tuple(random.choices(range(256), k=1))

            # Draw the rectangle
            rectangle_coords = (int(ab.xmin), int(ab.ymin), int(ab.xmax), int(ab.ymax))
            draw.rectangle(rectangle_coords, outline=255)

            # Add the text
            text_coords = (int(ab.xmin) - 5, int(ab.ymin) - 5)
            text = list_recognized[j + end]
            font = ImageFont.truetype(font_path, 40)
            draw.text(text_coords, text, fill=255, font=font)
        end += len(aabb)

        # Display the image
        plt.imshow(img, cmap='gray')
        plt.savefig("result_" + str(img_no) + ".png")
        img_no += 1
        plt.show()

    # if u want to delete crops
    shutil.rmtree(temp_folder)
    print(f"Deleted folder: {temp_folder}")


if __name__ == '__main__':
    interference()
